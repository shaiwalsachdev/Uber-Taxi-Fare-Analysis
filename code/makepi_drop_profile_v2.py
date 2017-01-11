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
def getPickupList(line,conread,taxilocation,outdict,locations):

    
   	with conread:
   		Q = "select pickup,timezone,count(pickup) from nyctaxi where pickup in {loc} group by pickup,timezone;"\
   		.format(loc = taxilocation)
   		df = pd.read_sql_query(Q,conread)

#    print "\tdf created"
#    print len(df)
	for l in locations:
		print l
		df_n = df.loc[df['pickup'] == l]
		if not df_n.empty:
			timezone = list(df_n['timezone'])
			count = list(df_n['count(pickup)'])
			count_dict = dict()
			for ii in range(24):
				count_dict[ii] = 0
			for i in range(len(timezone)):
				if count[i] < 5:
					count_dict[timezone[i]] = 0
				else:
					count_dict[timezone[i]] = count[i]
			
			result = []
			for key,value in count_dict.iteritems():
				result.append(value)
			flag = False
			for ii in result:
				if not ii == 0:
					flag = True
					break
			if flag == True:
				outdict[l]['pickup'] = result

	return outdict
	
#Returns the dropoff locations(Only popular ones are added to the result)
def getDropoffList(line,conread,taxilocation,outdict,locations):

   	
   	with conread:
   		Q = "select dropoff,timezone,count(dropoff) from nyctaxi where dropoff in {loc} group by dropoff,timezone;"\
   		.format(loc = taxilocation)
   		df = pd.read_sql_query(Q,conread)

#    print "\tdf created"
#    print len(df)

	for l in locations:
		print l
		df_n = df.loc[df['dropoff'] == l]
		if not df_n.empty:
			timezone = list(df_n['timezone'])
			count = list(df_n['count(dropoff)'])
			count_dict = dict()
			for ii in range(24):
				count_dict[ii] = 0
			for i in range(len(timezone)):
				if count[i] < 5:
					count_dict[timezone[i]] = 0
				else:
					count_dict[timezone[i]] = count[i]
				
			
			result = []
			for key,value in count_dict.iteritems():
				result.append(value)
			
			flag = False
			for ii in result:
				if not ii == 0:
					flag = True
					break
			if flag == True:
				outdict[l]['dropoff'] = result


	return outdict


def main():

	start = int(sys.argv[1])
	end = int(sys.argv[2])
	
	#Connect with sql
	conread = sqlite3.connect("../../dataset/manhattan_withTime_pathmatched_algo2_YTF.sqlite")
	#getting locations from sqlite
	locations = getLocList(start,end)

	#Make loclist
	loclist = '('
	for ll in locations:
		loclist = loclist + '"'+str(ll)+'",'                                    

	taxilocation = loclist[:-1]+')'
	


	
	#Make a dictionary empty
	outdict = {}
	for i in locations:
		outdict[i] = dict()
		outdict[i]['pickup'] = 'null'
		outdict[i]['dropoff'] = 'null'
	

	outdict = getPickupList(i,conread,taxilocation,outdict,locations)
	outdict = getDropoffList(i,conread,taxilocation,outdict,locations)
	print taxilocation
	
	outfilename = '../pi_drop_profile/profiles_json/pi_drop_profile'+'_sid'+str(start)+'_eid'+str(end)+'.json.gz'
	with gzip.open(outfilename,'w') as jfout:
		json.dump(outdict,jfout)
	
	print "done"



if __name__=='__main__':
	main()