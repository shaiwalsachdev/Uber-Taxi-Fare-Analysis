import json
import gzip
import sqlite3
import pandas as pd
import sys
#Using the union of pickup and dropoff locations and pickuping up the locations(lat_long)
def getLocList(startid,endid):

    idlow = startid
    idhi = endid

    conread = sqlite3.connect("../pi_drop_profile/pi_drop_union.sqlite")

    with conread:
        
        Q = 'select * from locind where id >={qidlow} and id <={qidhi}'\
        .format(qidlow=idlow,qidhi=idhi)
           
        df = pd.read_sql_query(Q,conread)

#    print "\tdf created"
#    print len(df)
    loclist = list(df['location'])
    return loclist

#Returns the pickup locations(Only popular ones are added to the result)
def getPickupList(line,conread):

   
   	with conread:
   		Q = "select timezone,count(pickup) cnt from nyctaxi where pickup = \'{loc}\' group by timezone having cnt > 5"\
   		.format(loc = line)
   		df = pd.read_sql_query(Q,conread)

#    print "\tdf created"
#    print len(df)

	timezone = list(df['timezone'])
	count = list(df['cnt'])
	count_dict = dict()
	if len(timezone)==0:
		return 'null'
	for i in range(24):
		count_dict[i] = 0
	for i in range(len(timezone)):
		count_dict[timezone[i]] = count[i]

	result = []
	for key,value in count_dict.iteritems():
		result.append(value)
	
	return result
#Returns the dropoff locations(Only popular ones are added to the result)
def getDropoffList(line,conread):

   	
   	with conread:
   		Q = "select timezone,count(dropoff) cnt from nyctaxi where dropoff = \'{loc}\' group by timezone having cnt > 5"\
   		.format(loc = line)
   		df = pd.read_sql_query(Q,conread)

#    print "\tdf created"
#    print len(df)
	
	timezone = list(df['timezone'])
	count = list(df['cnt'])
	count_dict = dict()
	if len(timezone)==0:
		return 'null'
	for i in range(24):
		count_dict[i] = 0
	for i in range(len(timezone)):
		count_dict[timezone[i]] = count[i]

	result = []
	for key,value in count_dict.iteritems():
		result.append(value)
	
	return result


def main():

	start = int(sys.argv[1])
	end = int(sys.argv[2])
	
	#Connect with sql
	conread = sqlite3.connect("../../dataset/manhattan_withTime_pathmatched_algo2_YTF.sqlite")
	#getting locations from sqlite
	locations = getLocList(start,end)

	#Visited Json for pickup locations
	injson1 = '../pi_drop_profile/pickup.json'
	with open(injson1,'r') as jfin:
		pickup = json.load(jfin)

	#Visited Json for dropoff locations
	injson1 = '../pi_drop_profile/dropoff.json'
	with open(injson1,'r') as jfin:
		dropoff = json.load(jfin)


	outdict = {}
	for i in locations:
		
		

		if(pickup.has_key(i)):
			pi = getPickupList(i,conread)
		else:
			pi  = 'null'
		if(dropoff.has_key(i)):
			di = getDropoffList(i,conread)
		else:
			di = 'null'
		print i
		if not (pi=='null' and di == 'null'):
			outdict[i] = {}
			outdict[i]['pickup'] = pi
			outdict[i]['dropoff'] = di
	outfilename = '../pi_drop_profile/profiles_json/pi_drop_profile'+'_sid'+str(start)+'_eid'+str(end)+'.json.gz'
	with gzip.open(outfilename,'w') as jfout:
		json.dump(outdict,jfout)




if __name__=='__main__':
	main()