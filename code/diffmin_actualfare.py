#To find how many times it happens that fare was less than min and customer had to pay the minimumn fare
#Thus Uber generating profit out of it.

#uberPOOL,uberX,uberXL,uberFAMILY,UberBLACK,UberSUV vs NYC Data
import json
import gzip
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
plt.switch_backend('agg')


def getcdf(freq):
	#Making a cumualtive distributin function
	#frequency is in terms of dictionary freq
	#divide the count by the sum of count of all frequencies
	#FInd the cumulative sum of probalities
	#function returns the [xaxis,yaxis] =[list of difference in fare,their culumative probabilities]
	xaxis = []
	yaxis = []
	
	sum_values = 0

	keys = []
	for key,value in freq.iteritems():
		keys.append(key)
		sum_values = sum_values + value

	keys.sort()
	for i in keys:
		xaxis.append(i)
		yaxis.append(float(float(freq[i])/float(sum_values)))
		
	for i in range(len(yaxis)):
		if i == 0:
			continue;
		else:
			yaxis[i] = yaxis[i] + yaxis[i-1]

	for i in range(len(yaxis)):
		yaxis[i] = float("{0:.6f}".format(yaxis[i]))
	return [xaxis,yaxis]


def main():
	
	#Read the Uber data for all four timezones 6,10,16,20
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

	#Plot Timezone6  with red and other colors so on.
	colors = {0:'red',1:'blue',2:'green',3:'magenta'}

	fig = plt.figure() 
	ax = fig.add_subplot(111)
	red_patch1 = mpatches.Patch(color='red', label='Timezone 6')
	red_patch2 = mpatches.Patch(color='blue', label='Timezone 10')
	red_patch3 = mpatches.Patch(color='green', label='Timezone 16')
	red_patch4 = mpatches.Patch(color='magenta', label='Timezone 20')
	ax.set_ylim([0.0,1])

	diff_uber = dict()
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
				
				#Here checking the condition
				if mini > uber_x:
					value = int(round(float(mini-uber_x)))
					if diff_uber.has_key(value):
						c =  diff_uber[value]
						c = c + 1
						diff_uber[value] = c
					else:
						diff_uber[value] = 1
				
			line = infile.readline()

	print diff_uber
	[xaxis,yaxis] = getcdf(diff_uber)
	print xaxis
	print yaxis
	plt.plot(xaxis,yaxis,color = 'red')

	diff_uber = dict()
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
				if mini > uber_x:
					value = int(round(float(mini-uber_x)))
					if diff_uber.has_key(value):
						c =  diff_uber[value]
						c = c + 1
						diff_uber[value] = c
					else:
						diff_uber[value] = 1		
				
			line = infile.readline()

	print diff_uber
	[xaxis,yaxis] = getcdf(diff_uber)
	print xaxis
	print yaxis
	plt.plot(xaxis,yaxis,color = 'blue')

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
				
				if mini > uber_x:
					value = int(round(float(mini-uber_x)))
					if diff_uber.has_key(value):
						c =  diff_uber[value]
						c = c + 1
						diff_uber[value] = c
					else:
						diff_uber[value] = 1			
				
			line = infile.readline()
	print diff_uber
	[xaxis,yaxis] = getcdf(diff_uber)
	print xaxis
	print yaxis
	plt.plot(xaxis,yaxis,color = 'green')
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
				
				if mini > uber_x:
					value = int(round(float(mini-uber_x)))
					if diff_uber.has_key(value):
						c =  diff_uber[value]
						c = c + 1
						diff_uber[value] = c
					else:
						diff_uber[value] = 1			
				
			line = infile.readline()
	print diff_uber
	[xaxis,yaxis] = getcdf(diff_uber)
	print xaxis
	print yaxis
	plt.plot(xaxis,yaxis,color = 'magenta')

	plt.legend(handles=[red_patch1,red_patch2,red_patch3,red_patch4],loc = 4)
	fig.suptitle('For UberX',fontsize = 20,fontweight='bold')
	ax.set_xlabel('Difference(mini - uber_actual)',fontsize = 20,fontweight='bold')
	ax.set_ylabel('CDF',fontsize = 20,fontweight='bold')	
	#plt.tight_layout()
	fig.savefig('../candidates/diffmin_actualfare.pdf')
	#Plotting all the four curves on the same map for different timezones
	

			




if __name__=='__main__':
	main()