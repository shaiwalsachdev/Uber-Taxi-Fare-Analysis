#uberPOOL,uberX,uberXL,uberFAMILY,UberBLACK,UberSUV vs NYC Data
import json
import gzip
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
plt.switch_backend('agg')
#We wanted to validate the 8*surcharge for UberX == Minimum fare
def getcdf(freq):
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
	
	injson1 = '/home/sankarshan/shaiwal/Uber/ByTimezone/20/20uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber = json.load(jfin)
	'''
	injson1 = '/home/sankarshan/shaiwal/Uber/ByTimezone/10/10uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber1 = json.load(jfin)

	injson1 = '/home/sankarshan/shaiwal/Uber/ByTimezone/16/16uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber2 = json.load(jfin)

	injson1 = '/home/sankarshan/shaiwal/Uber/ByTimezone/20/20uberprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		uber3 = json.load(jfin)
	'''
	
	candidates = []
	with open('//home/sankarshan/shaiwal/Uber/ByTimezone/20/nyc_taxi/zone20_loc.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			candidates.append(line)
			line = infile.readline()
			
	
	#diff_dict = {0:'diff_pool' , 1:'diff_x',2:'diff_xl',3:'diff_family',4:'diff_black',5:'diff_suv'}
	colors = {0:'red',1:'blue',2:'green',3:'magenta'}

	fig = plt.figure() 
	ax = fig.add_subplot(111)
	red_patch1 = mpatches.Patch(color='red', label='Timezone 6')
	red_patch2 = mpatches.Patch(color='blue', label='Timezone 10')
	red_patch3 = mpatches.Patch(color='green', label='Timezone 16')
	red_patch4 = mpatches.Patch(color='magenta', label='Timezone 20')


	ax.set_ylim([0.0,1])

	#Plot Timezone 6
	diff_uber = dict()
	for j in candidates:
		if uber[j].has_key('prices'):
			mini = float(uber[j]['prices'][1]['minimum'])
			print mini
			surcharge = float(uber[j]['prices'][1]['surge_multiplier'])*8
			print surcharge
			value = int(round(surcharge-mini))
			print value
			if diff_uber.has_key(value):
				c =  diff_uber[value]
				c = c + 1
				diff_uber[value] = c
			else:
				diff_uber[value] = 1
	
	print diff_uber
	[xaxis,yaxis] = getcdf(diff_uber)
	print xaxis
	print yaxis
	plt.plot(xaxis,yaxis,color = 'red')
		

	plt.legend(handles=[red_patch1,red_patch2,red_patch3,red_patch4],loc = 3)
	fig.suptitle('Validate MinFare = 8*surcharge for UberX',fontsize = 20,fontweight='bold')
	ax.set_xlabel('Difference(8*surcharge - Minimum)',fontsize = 20,fontweight='bold')
	ax.set_ylabel('CDF',fontsize = 20,fontweight='bold')	
	#plt.tight_layout()
	fig.savefig('/home/sankarshan/shaiwal/Uber/ByTimezone/candidates/minfare_validate.pdf')
			


if __name__=='__main__':
	main()