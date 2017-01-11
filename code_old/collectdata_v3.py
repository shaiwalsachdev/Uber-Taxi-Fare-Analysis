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
	
	#GET the url
	try:
		with eventlet.Timeout(10):
			response = requests.get(url,proxies=proxyDict,params=parameters)
		#response = requests.get(url,params=parameters)
	except ConnectionError: 
		time.sleep(4)
		with eventlet.Timeout(10):
			response = requests.get(url,proxies=proxyDict,params=parameters)
		#response = requests.get(url,params=parameters)
	
	#print response.url
	#response data in json
	#data = response.json()
	return response.text
	#return data.text

#The Time Estimates endpoint returns ETAs for all products currently available at a given location 
#lat_long take start_latitude and start_longitude as parameters

def getLocList(startid,endid):

    idlow = startid
    idhi = endid

    conread = sqlite3.connect("../dataset/testlocation10000.sqlite")

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

	outjsonfile = 'api_keys.json'
	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	output = [] 

	for l in loclist:
		line = l 
		line=line.strip()
		print line 
		output.append(uber_getprice(keys[keyid],line))

	outfilename = '../output/uberprice_key'+str(keyid)+'_sid'+str(idlow)+'_eid'+str(idhi)+'.txt.gz'	
	with gzip.open(outfilename, 'w') as outputfile:
		for i in output:
			outputfile. write(i) 
			outputfile. write(' \n')

	
#Now Generate the data showing the start_lat,start_long,end_lat,end_long,price_estimate,duration,distance,time_estimate_for_start





if __name__=="__main__":
    main()

