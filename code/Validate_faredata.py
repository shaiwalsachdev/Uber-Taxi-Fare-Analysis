#uberPOOL,uberX,uberXL,uberFAMILY,UberBLACK,UberSUV vs NYC Data
import json
import gzip
#test of our mathematical equations
#Minimum Fare = Base_minfare * surcharge
def main():
	'''
	fare= (base fare + (price/distance)*distacnce + (price/minute)*(minutes))*surcharge

	if fare < minimum:
  fare = minimum

	This final fare 
	check
	lies between the Low Estimate and High estimate.
	If yes, keep count of it and print the percentage
	'''
	injson1 = '../6/6uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber = json.load(jfin)

	injson1 = '../10/10uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber1 = json.load(jfin)

	injson1 = '../16/16uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber2 = json.load(jfin)

	injson1 = '../20/20uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber3 = json.load(jfin)

	counter = 0
	counter1 = 0
	counter2 = 0
	
	with open('../6/nyc_taxi/zone6_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber[line].has_key('prices')):
				
				high = float(uber[line]['prices'][1]['high_estimate'])
				
				low = float(uber[line]['prices'][1]['low_estimate'])
				surcharge = float(uber[line]['prices'][1]['surge_multiplier'])
				
				uber_x = 2.55 + (0.35)*(float(uber[line]['prices'][1]['duration'])/60) +(1.75)*float(uber[line]['prices'][1]['distance']);
				uber_x = surcharge*uber_x
				mini = float(uber[line]['prices'][1]['minimum'])

				if uber_x < 8*surcharge:
					uber_x = 8*surcharge
				if uber_x < low:
					counter =counter + 1
				elif uber_x >= low and uber_x <= high:
					counter1 = counter1 + 1
				elif uber_x > high:
					counter2 = counter2 + 1			
				
			line = infile.readline()

	with open('../10/nyc_taxi/zone10_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber1[line].has_key('prices')):
				
				high = float(uber1[line]['prices'][1]['high_estimate'])
				
				low = float(uber1[line]['prices'][1]['low_estimate'])
				surcharge = float(uber1[line]['prices'][1]['surge_multiplier'])
				uber_x = 2.55 + (0.35)*(float(uber1[line]['prices'][1]['duration'])/60) +(1.75)*float(uber1[line]['prices'][1]['distance']);
				uber_x = surcharge*uber_x
				mini = float(uber1[line]['prices'][1]['minimum'])
				if uber_x < 8*surcharge:
					uber_x = 8*surcharge
				if uber_x < low:
					counter =counter + 1
				elif uber_x >= low and uber_x <= high:
					counter1 = counter1 + 1
				elif uber_x > high:
					counter2 = counter2 + 1			
				
			line = infile.readline()
	with open('../16/nyc_taxi/zone16_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber2[line].has_key('prices')):
				
				high = float(uber2[line]['prices'][1]['high_estimate'])
				
				low = float(uber2[line]['prices'][1]['low_estimate'])
				surcharge = float(uber2[line]['prices'][1]['surge_multiplier'])
				
				uber_x = 2.55 + (0.35)*(float(uber2[line]['prices'][1]['duration'])/60) +(1.75)*float(uber2[line]['prices'][1]['distance']);
				uber_x = surcharge*uber_x
				mini = float(uber2[line]['prices'][1]['minimum'])
				if uber_x < 8*surcharge:
					uber_x = 8*surcharge
				if uber_x < low:
					counter =counter + 1
				elif uber_x >= low and uber_x <= high:
					counter1 = counter1 + 1
				elif uber_x > high:
					counter2 = counter2 + 1			
				
			line = infile.readline()

	with open('../20/nyc_taxi/zone20_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber3[line].has_key('prices')):
				
				high = float(uber3[line]['prices'][1]['high_estimate'])
				
				low = float(uber3[line]['prices'][1]['low_estimate'])
				surcharge = float(uber3[line]['prices'][1]['surge_multiplier'])
				
				uber_x = 2.55 + (0.35)*(float(uber3[line]['prices'][1]['duration'])/60) +(1.75)*float(uber3[line]['prices'][1]['distance']);
				uber_x = surcharge*uber_x
				mini = float(uber3[line]['prices'][1]['minimum'])
				if uber_x < 8*surcharge:
					uber_x = 8*surcharge
				if uber_x < low:
					counter =counter + 1
				elif uber_x >= low and uber_x <= high:
					counter1 = counter1 + 1
				elif uber_x > high:
					counter2 = counter2 + 1			
				
			line = infile.readline()


	total = counter+counter1+counter2
	print total
	print counter
	print "Percentage of Fare less than low estimate = " 
	print (float(counter)/float(total))*100
	print counter1
	print "Percentage of Fare b/w  low & high estimate = " 
	print (float(counter1)/float(total))*100
	print counter2
	print "Percentage of Fare greater than high estimate = " 
	print (float(counter2)/float(total))*100
			




if __name__=='__main__':
	main()