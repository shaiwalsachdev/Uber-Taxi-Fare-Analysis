import time
import os
import json
import requests
import sys
import pandas as pd
import numpy as np
import gzip
from requests.exceptions import ConnectionError
import sqlite3

#Fucntion takes a server_token and line(OD pair) and returns the json response
def lyft_getprice(server_token,line):
	
	lat_long = line.split('_')
	url = 'https://api.lyft.com/v1/cost'
	token  = 'bearer ' + server_token
	headers = {"Authorization": token}

	http_proxy  = "http://10.3.100.207:8080"
	https_proxy = "https://10.3.100.207:8080"

	proxyDict = {"http"  : http_proxy,"https" : https_proxy}

	parameters = {
	'start_lat': lat_long[0],
	'start_lng': lat_long[1],
	'end_lat': lat_long[2],
	'end_lng': lat_long[3],
	}
	response = None

	while response is None:
		try:
			response = requests.get(url,proxies=proxyDict,headers=headers,params=parameters).json()
		except:
			pass
	return response
	
def getLocList(startid,endid):

    idlow = startid
    idhi = endid

    conread = sqlite3.connect("/home/sankarshan/shaiwal/Uber/ByTimezone/candidates/candidates_intersection.sqlite")

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
	timezone = int(sys.argv[4])

	#getting locations from sqlite
	loclist = getLocList(idlow,idhi)

	outjsonfile = '/home/sankarshan/shaiwal/Uber/ByTimezone/code/lyft_keys.json'
	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	
	outdict = {}
	#Output key as OD pair and value as json response 
	for l in loclist:
		line = l 
		line=line.strip()
		print line 
		outdict[line]=lyft_getprice(keys[keyid],line)
		#print outdict[line]

	outfilename = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/lyft/'+str(timezone)+'lyftprice_key'+str(keyid)+'_sid'+str(idlow)+'_eid'+str(idhi)+'.json.gz'
	with gzip.open(outfilename,'w') as jfout:
		json.dump(outdict,jfout)

	
if __name__=="__main__":
    main()
