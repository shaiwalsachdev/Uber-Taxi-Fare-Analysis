#Collect the UBER fare data for OD pairs which lie in timezone 16
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


#Function to get the estimated uber fare giving input the parameters
#server_token is the key required by the UBER API
#line is basically a OD pair is  of the four parameters start_latitude,start_longitude,end_latitude,end_longitude
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
	

#Get the OD pair between startid and endid
def getLocList(startid,endid):

    idlow = startid
    idhi = endid

    conread = sqlite3.connect("/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/dataset/sqlite/zone16_loc.sqlite")

    with conread:
        
        Q = 'select * from locind where id >={qidlow} and id <={qidhi}'\
        .format(qidlow=idlow,qidhi=idhi)
           
        df = pd.read_sql_query(Q,conread)

#    print "\tdf created"
#    print len(df)
    loclist = list(df['location'])
    return loclist


#Function to read data and generate the json response file
def main():
	#Read the given file line by line

	keyid = str(sys.argv[1])
	idlow = int(sys.argv[2])
	idhi = int(sys.argv[3])


	#getting locations from sqlite
	loclist = getLocList(idlow,idhi)

	outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/api_keys1.json'
	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	
	outdict = {}
	#Adding the response for each OD pair to the dictionary
	for l in loclist:
		line = l 
		line=line.strip()
		print line 
		outdict[line]=uber_getprice(keys[keyid],line)
	#Writing the result to a zipped json file 
	outfilename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/16/uber/16uberprice_key'+str(keyid)+'_sid'+str(idlow)+'_eid'+str(idhi)+'.json.gz'
	with gzip.open(outfilename,'w') as jfout:
		json.dump(outdict,jfout)

		
	

	

if __name__=="__main__":
    main()

