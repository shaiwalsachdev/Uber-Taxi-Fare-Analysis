from __future__ import division
#Importing Packages
import requests
import json
import sys
import pandas as pd
import numpy as np
import gzip
import time
from requests.exceptions import ConnectionError
import sqlite3
import eventlet
#Simple side by side comparison 
#Send the test location to the UBER API and get surcharge
#Compare it with the estimated average surcharge of the hour
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
from sklearn.cross_validation import KFold

#Function to get the price giving input the parameters
#Run the function for each line of input file that is for each of source destination co-ordinates given
#lat_long is a list of the four parameters start_latitude,start_longitude,end_latitude,end_longitude
def uber_getprice(server_token,line):
	lat_long = line.split('_')
	url = 'https://api.uber.com/v1/estimates/price'
	
	http_proxy  = "http://10.3.100.207:8080"
	https_proxy = "https://10.3.100.207:8080"

	proxyDict = {"http"  : http_proxy,"https" : https_proxy}

	parameters = {
	'server_token': server_token,
	'start_latitude': lat_long[0],
	'start_longitude': lat_long[1],
	'end_latitude': lat_long[2],
	'end_longitude': lat_long[3],
	}
	
	response = None
	while response is None:
		try:
			response = requests.get(url,proxies=proxyDict,params=parameters)
		except:
			pass
	return response.text
	

def generate_csv(timezone,uber_service):
	injson = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/pi_drop_profile/pi_drop_merged.json.gz'
	with gzip.open(injson,'r') as jfin:
		pi_drop = json.load(jfin)

	injson1 = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/'+str(timezone)+'uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber2 = json.load(jfin)

	latitude = []
	longitude = []
	popularity = []
	surcharge_mul = []
	
	with open('/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/nyc_taxi/zone'+str(timezone)+'_loc.txt','r') as infile:
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
	#Now , Same pickup location at same timezone (Take Average Surcharge)
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
	datacollected_new.to_csv('/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/estimator/'+str(timezone)+'_'+str(uber_service)+'lat_long_popularity_surcharge.csv',index = False)



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

			for i in range(len(weights)):
				weights[i] = weights[i]/summ

				
			pop_estimated = 0.0
			for l in range(len(poplist)):
				pop_estimated = pop_estimated + poplist[l]*weights[l]
			
			return pop_estimated

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
    return result


def surcharge_estimator_local(Train,latitude,longitude,popularity):
	radius = 0.1 #miles
	while radius <= 1.0:
		candidates,poplist = geo_search(latitude,longitude,radius,Train)
		if len(poplist) == 0:
			radius = radius + 0.1
		else:
			features = list(candidates.popularity)
			target = list(candidates.surcharge)
			datapoint = popularity
			answer = lwr_predict_idw(features,target,datapoint)
			break

	return answer


def main():
	#Read the given file line by line

	keyid = str(sys.argv[1])
	uber_service = int(sys.argv[2])
	timezone = int(sys.argv[3])

	loclist = []
	with open("/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/"+str(timezone)+"/test.txt","r") as infile:
		line = infile.readline()
		#print line
		while line:
			if line == '':
				break
			loclist.append(line)
			line = infile.readline()


	#print loclist



	outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/keys/api_keys1.json'
	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	PATH = "/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/estimator/"+str(timezone)+"_"+str(uber_service)+"lat_long_popularity_surcharge.csv"
	if not os.path.isfile(PATH):
		generate_csv(timezone,uber_service)
	
	Train = pd.read_csv("/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/estimator/"+str(timezone)+"_"+str(uber_service)+"lat_long_popularity_surcharge.csv")

	sur_real = []
	sur_est = []
	i = 0
	outdict = {}
	for line in loclist:
		if line == '':
			break
		i = i + 1
		print i
		outdict[line]=uber_getprice(keys[keyid],line)
		txttojson = json.loads(outdict[line])
		sur_r = txttojson['prices'][uber_service]['surge_multiplier']
		#print sur_r
		sur_real.append(sur_r)

		lat_long = line.split('_')

		pop_est = popularity_estimator_idw(float(lat_long[0]),float(lat_long[1]),Train)
		#print pop_est
		sur_e = surcharge_estimator_local(Train,float(lat_long[0]),float(lat_long[1]),pop_est)
		if sur_e < 1.0:
			sur_est.append(1.0)
		else:
			sur_est.append(sur_e)

		print sur_real
		print sur_est
		print "The MSE obtained  = %f" %(metrics.mean_squared_error(sur_real,sur_est))

	for i in range(len(sur_real)):
		print sur_real[i],sur_est[i]
	print "The MSE obtained  = %f" %(metrics.mean_squared_error(sur_real,sur_est))

	

	


if __name__=="__main__":
    main()