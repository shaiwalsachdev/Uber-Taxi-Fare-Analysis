import json
import gzip


def main():
	intials = '20uberprice_key'
	dict_20 = {}

	begin = 1
	window = 1256

	for i in range(1,201):
		keyid = i
		startid = begin
		endid = startid + window - 1

		filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/Outputfor20/20uberprice_key'+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json'
		
		with open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_20[key] = json.loads(value)

		begin = endid+1



	window = 10
	begin = 251201

	for i in range(1,12):
		keyid = i
		startid = begin
		endid = startid + window - 1
		filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/Outputfor20/20uberprice_key'+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json'
		with open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_20[key] = json.loads(value)

		begin = endid+1

	filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/Outputfor20/20uberprice_key'+str(12)+'_sid'+str(251311)+'_eid'+str(251318)+'.json'
	with open(filename,'r') as jfin:
		keys = json.load(jfin)

	for key, value in keys.iteritems():
		dict_20[key] = json.loads(value)
	outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/20/20uberprice.json.gz'

	with gzip.open(outjsonfile,'w') as jfout:
		json.dump(dict_20,jfout)
	

	#print json.loads(keys['40.756567_-73.990276_40.760418_-73.975831'])['prices'][0]['estimate']
	



if __name__=='__main__':
	main()