#Finds the percentage of data which has surcharge
import json
import gzip

def main():
	
	#Read all the collected uber data for 4 timezones

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


	#Initialize a counter to count the number of locations which have surcharge 
	#6
	counter = 0
	total = 0
	#10
	counter1 = 0
	total1 = 0
	#16
	counter2 = 0
	total2 = 0
	#20
	counter3 = 0
	total3 = 0

	#We will use the OD pair as key and get the json response which is its value 
	#From the json response get the surcharge value for UberX for all four timezones
	with open('../6/nyc_taxi/zone6_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber[line].has_key('prices')):
				total = total + 1
				
				surcharge = float(uber[line]['prices'][1]['surge_multiplier'])
				if surcharge > 1.0:
					counter = counter + 1 
					
			line = infile.readline()

	with open('../10/nyc_taxi/zone10_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber1[line].has_key('prices')):
				total1+=1
				
				surcharge = float(uber1[line]['prices'][1]['surge_multiplier'])
				if surcharge > 1.0:
					counter1+=1
				
			line = infile.readline()
	with open('../16/nyc_taxi/zone16_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber2[line].has_key('prices')):
				total2+=1
				
				surcharge = float(uber2[line]['prices'][1]['surge_multiplier'])
				if surcharge > 1.0:
					counter2+=1
						
				
			line = infile.readline()

	with open('../20/nyc_taxi/zone20_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			
			
			if(uber3[line].has_key('prices')):
				
				total3+=1
				surcharge = float(uber3[line]['prices'][1]['surge_multiplier'])
				if surcharge > 1.0:
					counter3+=1
						
				
			line = infile.readline()


	#Find the percentage of data which has surcharge > 1.0
	
	print "Percentage of surcharge Timezone 6 = " 
	print (float(counter)/float(total))*100
	print counter
	print total
	print "Percentage of surcharge Timezone 10 = " 
	print (float(counter1)/float(total1))*100
	print counter1
	print total1
	print "Percentage of surcharge Timezone 16 = " 
	print (float(counter2)/float(total2))*100
	print counter2
	print total2
	print "Percentage of surcharge Timezone 20 = " 
	print (float(counter3)/float(total3))*100
	print counter3
	print total3




if __name__=='__main__':
	main()