import json
import gzip


def main():
	intials = 'pi_drop_profile'
	dict_6 = {}

	begin = 1
	window = 114

	for i in range(1,201):
		startid = begin
		endid = startid + window - 1

		filename = '../pi_drop_profile/profiles_json/pi_drop_profile'+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
		with gzip.open(filename,'r') as jfin:
			keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_6[key] = value

		begin = endid + 1


	

	filename = '../pi_drop_profile/profiles_json/pi_drop_profile'+'_sid'+str(22801)+'_eid'+str(22911)+'.json.gz'
	with gzip.open(filename,'r') as jfin:
		keys = json.load(jfin)
	for key, value in keys.iteritems():
		dict_6[key] = value



	outjsonfile = '../pi_drop_profile/pi_drop_merged.json.gz'

	with gzip.open(outjsonfile,'w') as jfout:
		json.dump(dict_6,jfout)

	#print json.loads(keys['40.756567_-73.990276_40.760418_-73.975831'])['prices'][0]['estimate']
	



if __name__=='__main__':
	main()