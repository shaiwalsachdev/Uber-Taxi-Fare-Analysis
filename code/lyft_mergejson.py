import json
import gzip
import sys

def main():
	timezone = int(sys.argv[1])
	dict_6 = {}

	begin = 1
	window = 94

	for i in range(1,201):
		keyid = i
		startid = begin
		endid = startid + window - 1

		filename = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/lyft/'+str(timezone)+'lyftprice_key'+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
		with gzip.open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_6[key] = value

		begin = endid + 1
	window = 12
	begin = 18801

	for i in range(1,13):
		keyid = i
		startid = begin
		endid = startid + window - 1
		filename = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/lyft/'+str(timezone)+'lyftprice_key'+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
		with gzip.open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_6[key] =value 

		begin = endid+1


	outjsonfile = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/'+str(timezone)+'lyftprice.json.gz'

	with gzip.open(outjsonfile,'w') as jfout:
		json.dump(dict_6,jfout)

	#print json.loads(keys['40.756567_-73.990276_40.760418_-73.975831'])['prices'][0]['estimate']
	



if __name__=='__main__':
	main()