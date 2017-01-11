#To make a json file such that 
#key is OD pair
#Values are differece in fare between uber_x ,xl,family,black,suv minus nyc fare
#uberPOOL,uberX,uberXL,uberFAMILY,UberBLACK,UberSUV vs NYC Data
import json
import gzip

def main():
	
	#Get NYC FARE
	#zone10_loc_count_avg : contains the OD pair as key and values are Tripcount,avg_distance,duration,fare fro nyc.
	injson = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/nyc_taxi/zone10_loc_count_avg.json'
	with open(injson,'r') as jfin:
		nyc = json.load(jfin)



	#Get UBER FARE
	injson1 = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/10uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber = json.load(jfin)

	#this will be the output file
	outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/diff_zone10.json.gz'


	#Make a dictionary and dump it into json
	distribution = dict()
	with open('/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/nyc_taxi/zone10_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			nyc_fare = float(nyc[line]['avgfare'])
			
			if(uber[line].has_key('prices')):
				uber_pool = (float(uber[line]['prices'][0]['high_estimate']) +float(uber[line]['prices'][0]['low_estimate']))/2 - nyc_fare;
				uber_x = (float(uber[line]['prices'][1]['high_estimate']) +float(uber[line]['prices'][1]['low_estimate']))/2 - nyc_fare;
				uber_xl = (float(uber[line]['prices'][2]['high_estimate']) +float(uber[line]['prices'][2]['low_estimate']))/2 - nyc_fare;
				uber_family = (float(uber[line]['prices'][3]['high_estimate']) +float(uber[line]['prices'][3]['low_estimate']))/2 - nyc_fare;
				uber_black = (float(uber[line]['prices'][4]['high_estimate']) +float(uber[line]['prices'][4]['low_estimate']))/2 - nyc_fare;
				uber_suv = (float(uber[line]['prices'][5]['high_estimate']) +float(uber[line]['prices'][5]['low_estimate']))/2 - nyc_fare;

			distribution[line] = {'diff_pool':uber_pool , 'diff_x':uber_x,'diff_xl':uber_xl,'diff_family':uber_family,'diff_black':uber_black,'diff_suv':uber_suv}
			line = infile.readline()

	with gzip.open(outjsonfile,'w') as jfout:
		json.dump(distribution,jfout)
			




if __name__=='__main__':
	main()