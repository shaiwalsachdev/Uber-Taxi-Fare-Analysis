import json
import gzip


def main():
	intials = '10uberprice_key'
	dict_10 = {}

	begin = 1
	window = 1050

	for i in range(1,201):
		keyid = i
		startid = begin
		endid = startid + window - 1

		filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/uber/10uberprice_key'+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
		with gzip.open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_10[key] = json.loads(value)

		begin = endid+1

	window = 5
	begin = 210001

	for i in range(1,14):
		keyid = i
		startid = begin
		endid = startid + window - 1
		filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/uber/10uberprice_key'+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
		with gzip.open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_10[key] = json.loads(value)

		begin = endid+1


	outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/10uberprice.json.gz'

	with gzip.open(outjsonfile,'w') as jfout:
		json.dump(dict_10,jfout)

	#print json.loads(keys['40.756567_-73.990276_40.760418_-73.975831'])['prices'][0]['estimate']
	



if __name__=='__main__':
	main()