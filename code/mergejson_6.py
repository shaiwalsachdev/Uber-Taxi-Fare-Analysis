import json
import gzip


def main():
	intials = '6uberprice_key'
	dict_6 = {}

	begin = 1
	window = 317

	for i in range(1,201):
		keyid = i
		startid = begin
		endid = startid + window - 1

		filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/6/uber/6uberprice_key'+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
		with gzip.open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_6[key] = json.loads(value)

		begin = endid + 1



	filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/6/uber/6uberprice_key'+str(1)+'_sid'+str(63401)+'_eid'+str(63409)+'.json.gz'
	with gzip.open(filename,'r') as jfin:
		keys = json.load(jfin)

	for key, value in keys.iteritems():
		dict_6[key] = json.loads(value)


	outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/6/6uberprice.json.gz'

	with gzip.open(outjsonfile,'w') as jfout:
		json.dump(dict_6,jfout)

	#print json.loads(keys['40.756567_-73.990276_40.760418_-73.975831'])['prices'][0]['estimate']
	



if __name__=='__main__':
	main()