from __future__ import division
import json
import gzip
import sqlite3
import pandas as pd
import sys
import sqlite3
import csv
import os
import time
import numpy as np 
from geopy.distance import great_circle
import math
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
#https://blog.fedecarg.com/2009/02/08/geo-proximity-search-the-haversine-equation/#comment-4528
#http://www.arubin.org/files/geo_search.pdf
from sklearn import datasets, linear_model
from sklearn import metrics
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

def mse(est,real,thresh):
	e = est
	r = real
	#diff = set(list(abs(r-e)))
	#print sorted(diff)
	rr = []
	ee = []
	dd = list(abs(np.array(r)-np.array(e)))
	cnt = 0

	for i in xrange(len(dd)):
		if dd[i]<=thresh:
			rr.append(r[i])
			ee.append(e[i])
			cnt = cnt + 1

	rr = np.array(rr)
	ee = np.array(ee)

	mse = sum((rr-ee)*(rr-ee))/len(rr)
	return cnt,mse

def generate_csv(timezone,uber_service):
	#Generates the data for the timezone (pickup_lat,pickup_long,popularity,average surcharge)
	#First we read all the OD pairs 
	#take their surcharge
	#popularity will be taken from the pi_drop profile datainjson = '../pi_drop_profile/pi_drop_merged.json.gz'
	with gzip.open(injson,'r') as jfin:
		pi_drop = json.load(jfin)

	injson1 = '../'+str(timezone)+'/'+str(timezone)+'uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber2 = json.load(jfin)

	latitude = []
	longitude = []
	popularity = []
	surcharge_mul = []
	#If pickup location is in pi_Drop profile and  OD has surcharge value just add it
	with open('../'+str(timezone)+'/nyc_taxi/zone'+str(timezone)+'_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			lat_long  = line.split('_')
			pick = lat_long[0]+"_"+lat_long[1]
			
			if(uber2[line].has_key('prices') and pi_drop.has_key(pick)):
				if not pi_drop[pick]['pickup'] == 'null':
					#For Time zone 16
					x = int(pi_drop[pick]['pickup'][timezone-1])
					if not x == 0:
						latitude.append(float(lat_long[0]))
						longitude.append(float(lat_long[1]))
						#For Uber X
						surcharge = float(uber2[line]['prices'][uber_service]['surge_multiplier'])
						if surcharge == 1.0 :
							surcharge_mul.append(surcharge)
						else:
							surcharge_mul.append(surcharge)
						popularity.append(x)

			line = infile.readline()




	latitude = np.asarray(latitude)
	longitude = np.asarray(longitude)
	popularity = np.asarray(popularity)
	surcharge_mul = np.asarray(surcharge_mul)
	datacollected = pd.DataFrame({'latitude':latitude.transpose(),'longitude':longitude.transpose(),'popularity':popularity.transpose(),'surcharge':surcharge_mul.transpose()})
	
	#Remove duplicates rows (same location same surcharge)
	datacollected = datacollected.drop_duplicates()


	latitude_new = []
	longitude_new = []
	popularity_new = []
	surcharge_mul_new  = []
	#Now , Same pickup location , diff. values of surcharge (Take Average Surcharge)
	for index, row in datacollected.iterrows():
		sur = []
		condition_one = datacollected['latitude'] == row['latitude']
		condition_two = datacollected['longitude'] == row['longitude']
		dupli = datacollected[condition_one & condition_two]
		latitude_new.append(row['latitude'])
		longitude_new.append(row['longitude'])
		popularity_new.append(row['popularity'])
		surcharge_mul_new.append(np.mean(list(dupli['surcharge'])))
		dup_index  = list(dupli.index)
		datacollected.drop(dup_index)
		
	

	latitude_new = np.asarray(latitude_new)
	longitude_new = np.asarray(longitude_new)
	popularity_new = np.asarray(popularity_new)
	surcharge_mul_new = np.asarray(surcharge_mul_new)

	datacollected_new = pd.DataFrame({'latitude':latitude_new.transpose(),'longitude':longitude_new.transpose(),'popularity':popularity_new.transpose(),'surcharge':surcharge_mul_new.transpose()})
	datacollected_new.to_csv('../estimator/'+str(timezone)+'_'+str(uber_service)+'lat_long_popularity_surcharge.csv',index = False)


#Make a bounding box with latitude , longitude as center and radius and find all the neigbouring points which are in this box from the Train 
def geo_search(latitude,longitude,radius,Train):
	#Radius in miles
	lng_min = longitude - radius / abs(math.cos(math.radians(latitude)) * 69)
	lng_max = longitude + radius / abs(math.cos(math.radians(latitude)) * 69)
	lat_min = latitude - (radius / 69)
	lat_max = latitude + (radius / 69)
	#print 'lng (min/max): %f %f' % (lng_min, lng_max)
	#print 'lat (min/max): %f %f' % (lat_min, lat_max)
	
	
	
	condition_one = Train['latitude'] >= lat_min
	condition_two  = Train['latitude'] <= lat_max
	condition_three = Train['longitude'] >= lng_min
	condition_four = Train['longitude'] <= lng_max

	candidates = Train[condition_one & condition_two & condition_three & condition_four]
	
	poplist = list(candidates['popularity'])
	return [candidates,poplist]
#Normal Mean
def popularity_estimator(latitude,longitude,Train):
	radius = 0.1 #miles
	
	while radius <= 1.0:
		#Multiplication Factor
		if radius == 1.0:
			factor = 1.0
		else:
			factor = 1.0 - radius
		candidates,poplist = geo_search(latitude,longitude,radius,Train)
		if len(poplist) == 0:
			radius = radius + 0.1
			poplist = geo_search(latitude,longitude,radius,Train)
		else:
			return np.mean(poplist)*factor

#Using IDW #SIMPLE IDW (weight = inverse of square of great circle distance)

def popularity_estimator_idw(latitude,longitude,Train): #SIMPLE IDW
	radius = 0.1 #miles
	
	while radius <= 1.0:
		#Multiplication Factor
		if radius == 1.0:
			factor = 1.0
		else:
			factor = 1.0 - radius
		candidates,poplist = geo_search(latitude,longitude,radius,Train)
		if len(poplist) == 0:
			radius = radius + 0.1
			candidates,poplist = geo_search(latitude,longitude,radius,Train)
		else:
			nearpoints = []

			distance = []
			weights  = []
			#Find all the near points and great circle distance
			for index, row in candidates.iterrows():
				nearpoints.append((row['latitude'],row['longitude']))

			for ii in nearpoints:
				distance.append(great_circle(ii,(latitude,longitude)).miles)

			
			for jj in range(len(distance)):
				if distance[jj] == 0.0: 
					distance[jj] = radius/10000.0
					
				
			for j in distance:
				weights.append(1.0/(j*j))
				
			summ = 0.0
			for jj in weights:
				summ = summ + jj
			#Normalize the weights
			for i in range(len(weights)):
				weights[i] = weights[i]/summ

			#Do the weighted sum
			pop_estimated = 0.0
			for l in range(len(poplist)):
				pop_estimated = pop_estimated + poplist[l]*weights[l]
			
			return pop_estimated

#(better mothod) IDW with Modified Shepard's Method		
def popularity_estimator_idw_modified(latitude,longitude,Train): #Modified Shepard's Method
	radius = 0.1 #miles
	
	while radius <= 1.0:
		#Multiplication Factor
		if radius == 1.0:
			factor = 1.0
		else:
			factor = 1.0 - radius
		candidates,poplist = geo_search(latitude,longitude,radius,Train)
		if len(poplist) == 0:
			radius = radius + 0.1
			candidates,poplist = geo_search(latitude,longitude,radius,Train)
		else:
			nearpoints = []

			distance = []
			weights  = []
			
			for index, row in candidates.iterrows():
				nearpoints.append((row['latitude'],row['longitude']))

			for ii in nearpoints:
				distance.append(great_circle(ii,(latitude,longitude)).miles)

			
			for jj in range(len(distance)):
				if distance[jj] == 0.0: 
					distance[jj] = radius/10000.0
					
			for j in distance:
				xx = float(max(radius/10000,radius-j))
				yy = float(radius*j)
				weights.append(float(xx/yy)**2)

			summ = 0.0
			for jj in weights:
				summ = summ + jj

			for i in range(len(weights)):
				weights[i] = weights[i]/summ

				
			pop_estimated = 0.0
			for l in range(len(poplist)):
				pop_estimated = pop_estimated + poplist[l]*weights[l]
			
			return pop_estimated
#Decison Tree Regressor , finds the MSE for TEST locations
def surcharge_estimator(Train,Test):
	regr_1 = DecisionTreeRegressor(max_depth=3)
	featuresTrain =Train[["popularity"]]
	targetTrain  = Train[["surcharge"]]
	featuresTest =Test[["popularity"]]
	targetTest  = Test[["surcharge"]]
	regr_1.fit(featuresTrain, targetTrain)
	y_1 = regr_1.predict(featuresTest)
	

	target = list(targetTest['surcharge'])
	'''
	for i in range(len(y_1)):
		print y_1[i],target[i]
	'''
	print "The MSE obtained  = "
	print metrics.mean_squared_error(y_1,targetTest)

#Locally Weighted Regression on data X ,Y and X0= datapoint for which value is wanted(Normal Weight Function)
def lwr_predict_idw(x,y,datapoint):
    c = 1.0
    weights = []
    
    for i in range(len(x)):
        xx = float((x[i]-datapoint)*(x[i]-datapoint))
        if xx == 0:
        	yy = 1.0
        else:
        	yy = 1.0/xx

        if yy == 0:
        	weights.append(10 **-600)
        else:
			weights.append(yy)

    summ = 0
    for i in range(len(weights)):
    	summ = summ + x[i]*x[i]*weights[i]

    summ = 1.0/summ 


    summ1 = 0
    for i in range(len(weights)):
        summ1 = summ1 + x[i]*y[i]*weights[i]

    beta = summ*summ1
    result = beta*datapoint
    if math.isnan(result):
    	#print result
    	return 1.0
    else:
    	return result
#Locally Weighted Regression on data X ,Y and X0= datapoint for which value is wanted(Guassian Kernel)
def lwr_predict(x,y,datapoint):
    c = 1.0
    weights = []
    
    for i in range(len(x)):
        xx = float((x[i]-datapoint)*(x[i]-datapoint))
        yy = math.exp((xx)/(-2.0* c**2))
       	weights.append(yy)

    summ = 0
    for i in range(len(weights)):
    	summ = summ + x[i]*x[i]*weights[i]

    summ = 1.0/summ 


    summ1 = 0
    for i in range(len(weights)):
        summ1 = summ1 + x[i]*y[i]*weights[i]

    beta = summ*summ1
    result = beta*datapoint
    #if math.isnan(result):
    	#print result
    	#return 1.0
    #else:
    return result
#Find the MSE using the LWR
def surcharge_estimator_local(Train,Test):
	featuresTest =Test[["latitude","longitude","popularity"]]
	targetTest  = Test[["surcharge"]]
	y_1 = []
	for index,row in featuresTest.iterrows():
		radius = 0.1 #miles
		while radius <= 1.0:
			candidates,poplist = geo_search(row['latitude'],row['longitude'],radius,Train)
			if len(poplist) == 0:
				radius = radius + 0.1
			else:
				features = list(candidates.popularity)
				target = list(candidates.surcharge)
				datapoint = row['popularity']
				y_1.append(lwr_predict_idw(features,target,datapoint))
				break



	target1 = list(targetTest['surcharge'])

	
	for i in range(len(y_1)):
		print y_1[i],target1[i]
	
	print "The MSE obtained  = "
	target = list(targetTest['surcharge'])
	print metrics.mean_squared_error(list(y_1),targetTest)

#SVM regression
def surcharge_estimator_svm(Train,Test):
	
	featuresTrain =Train[["popularity"]]
	targetTrain  = Train[["surcharge"]]
	featuresTest =Test[["popularity"]]
	targetTest  = Test[["surcharge"]]
	clf = SVR(C=1.0, epsilon=0.2)
	clf.fit(featuresTrain, targetTrain)
	y_1 = clf.predict(featuresTest)
	

	target = list(targetTest['surcharge'])
	'''
	for i in range(len(y_1)):
		print y_1[i],target[i]
	'''
	print "The MSE obtained  = "
	print metrics.mean_squared_error(list(y_1),targetTest)

#KNN regression
def surcharge_estimator_knn(Train,Test):
	
	featuresTrain =Train[["popularity"]]
	targetTrain  = Train[["surcharge"]]
	featuresTest =Test[["popularity"]]
	targetTest  = Test[["surcharge"]]
	neigh = KNeighborsRegressor(n_neighbors=15)
	neigh.fit(featuresTrain, targetTrain)
	y_1 = neigh.predict(featuresTest)
	

	target = list(targetTest['surcharge'])
	'''
	for i in range(len(y_1)):
		print y_1[i],target[i]
		'''
	print "The MSE obtained  = "
	print metrics.mean_squared_error(y_1,targetTest)

#linear Regression
def surcharge_estimator_linear(Train,Test):
	
	featuresTrain =Train[["popularity"]]
	targetTrain  = Train[["surcharge"]]
	featuresTest =Test[["popularity"]]
	targetTest  = Test[["surcharge"]]
	regr = linear_model.LinearRegression()
	regr.fit(featuresTrain, targetTrain)
	y_1 = regr.predict(featuresTest)
	

	target = list(targetTest['surcharge'])
	'''
	for i in range(len(y_1)):
		print y_1[i],target[i]
		'''
	#print "The MSE obtained  = "
	print metrics.mean_squared_error(y_1,targetTest)

def main():
	timezone = int(sys.argv[1])
	uber_service = int(sys.argv[2])
	PATH = "../estimator/"+str(timezone)+"_"+str(uber_service)+"lat_long_popularity_surcharge.csv"
	if not os.path.isfile(PATH):
		generate_csv(timezone,uber_service)
	
	datainput = pd.read_csv("../estimator/"+str(timezone)+"_"+str(uber_service)+"lat_long_popularity_surcharge.csv")
	

	#Split data into two parts
	Train,Test = train_test_split(datainput,test_size = 0.20)

	#Check Population Estimator
	features = Train[["latitude","longitude","popularity"]]
	
	est_pop = []
	realpop = []
	for index, row in Test.iterrows():
		x =  popularity_estimator_idw_modified(row['latitude'],row['longitude'],Train)
		#print x,row['popularity']
		realpop.append(row['popularity'])
		est_pop.append(x)


	print "The MSE obtained  = %f" %(metrics.mean_squared_error(est_pop,realpop))
	cnt,mseval = mse(est_pop,realpop,10)
	print "our mse: %f" %(mseval)
	print cnt
	print len(est_pop)
	print "outliar: %f " %(1-float(cnt)/float(len(est_pop)))

	est_pop = np.asarray(est_pop)



	#Check Surcharge Estimator
	features1 = Train[["latitude","longitude","popularity","surcharge"]]
	target  = list(Test.surcharge)
	target = np.asarray(target)
	lat_list  = list(Test.latitude)
	lng_list  = list(Test.longitude)
	lat_list = np.asarray(lat_list)
	lng_list = np.asarray(lng_list)
	#Make a new dataframe using the estimated popularites and lat_long,surcharge of the test locations.
	test_new = pd.DataFrame({'latitude':lat_list.transpose(),'longitude':lng_list.transpose(),'popularity':est_pop.transpose(),'surcharge':target.transpose()})
	#call the function to print the MSE for surcharge
	surcharge_estimator_linear(features1,test_new)
	

	#Isotonic Regression:
	#http://tullo.ch/articles/speeding-up-isotonic-regression/
	#http://nbviewer.jupyter.org/urls/gist.githubusercontent.com/mjbommar/6b355ecfeb60051c799c/raw/isotonic-regressions-in-scikit-learn.ipynb

	
	

	


if __name__=='__main__':
	main()