#Suppose we apply SVM on location and surcharge(Yes or No)(2 classes)
#uberPOOL,uberX,uberXL,uberFAMILY,UberBLACK,UberSUV vs NYC Data
import json
import gzip
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt 
from sklearn  import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
import csv

from sklearn import metrics
def main():
	
	injson1 = '../16/16uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber2 = json.load(jfin)

	latitude = []
	longitude = []
	surcharge_mul = []
	
	with open('../16/nyc_taxi/zone16_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber2[line].has_key('prices')):
				
				lat_long  = line.split('_')
				surcharge = float(uber2[line]['prices'][1]['surge_multiplier'])
				latitude.append(float(lat_long[0]))
				longitude.append(float(lat_long[1]))
				if surcharge > 1.0:
					surcharge_mul.append(1)
				else:
					surcharge_mul.append(0)
						
			
			line = infile.readline()

	

	
	latitude1 = np.asarray(latitude)
	longitude1 = np.asarray(longitude)
	surcharge_mul1 = np.asarray(surcharge_mul)
	#Now apply SVM
	datacollected = pd.DataFrame({'latitude':latitude1.transpose(),'longitude':longitude1.transpose(),'surcharge':surcharge_mul1.transpose()})
	features = datacollected[["latitude","longitude"]]
	
	targetVariables =  datacollected.surcharge
	
	featureTrain,featuresTest,targetTrain,targetTest = train_test_split(features,targetVariables,test_size = 0.20)
	#print featureTrain
	#print targetTrain
	model  =  svm.SVC()
	fittedmodel = model.fit(featureTrain,targetTrain)
	predictions = fittedmodel.predict(featuresTest)
	s= accuracy_score(targetTest,predictions)
	print s



if __name__=='__main__':
	main()