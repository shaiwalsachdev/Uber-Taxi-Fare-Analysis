#uberPOOL,uberX,uberXL,uberFAMILY,UberBLACK,UberSUV vs NYC Data
#Finding the common locations between the four timezones and using these candidated we can plot the difference  fare distributon 
import json
import gzip
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib
import pylab
plt.switch_backend('agg')

#Cumulative Distributin Function
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
	font = {'weight' : 'bold'}
	matplotlib.rc('font', **font)

	inf= '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/diff_zone10.json.gz'
	with gzip.open(inf,'r') as jfin:
		data6 = json.load(jfin)

	
	candidates = []
	with open('/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/candidates/candidates_intersection.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			candidates.append(line)
			line = infile.readline()
			
	
	diff_dict = {0:'diff_pool' , 1:'diff_x',2:'diff_xl',3:'diff_family',4:'diff_black',5:'diff_suv'}
	colors = {0:'red',1:'blue',2:'green',3:'magenta',4:'black',5:'orangered'}

	fig = plt.figure() 
	ax = fig.add_subplot(111)
	red_patch1 = mpatches.Patch(color='red', label='diff_pool')
	red_patch2 = mpatches.Patch(color='blue', label='diff_x')
	red_patch3 = mpatches.Patch(color='green', label='diff_xl')
	red_patch4 = mpatches.Patch(color='magenta', label='diff_family')
	red_patch5 = mpatches.Patch(color='black', label='diff_black')
	red_patch6 = mpatches.Patch(color='orangered', label='diff_suv')

	ax.set_ylim([0.0,1])
	for i in range(6):
		diff_uber = dict()
		for j in candidates:
			if(data6.has_key(j)):
				value = int(round(float(data6[j][diff_dict[i]])))
				if diff_uber.has_key(value):
					c =  diff_uber[value]
					c = c + 1
					diff_uber[value] = c
				else:
					diff_uber[value] = 1
		[xaxis,yaxis] = getcdf(diff_uber)
		print xaxis
		print yaxis
		plt.plot(xaxis,yaxis,linewidth=3,color = colors[i])
		
		

	plt.legend(handles=[red_patch1,red_patch2,red_patch3,red_patch4,red_patch5,red_patch6],loc = 4)
	#fig.suptitle('Hour 20',fontsize = 20,fontweight='bold')
	ax.set_xlabel('Difference(USD)',fontsize = 20,fontweight='bold')
	ax.set_ylabel('CDF',fontsize = 20,fontweight='bold')	
	#plt.tight_layout()
	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
		item.set_fontsize(20) 

	pylab.tight_layout()    
	fig.savefig('/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/plots/diff_uber_10_v2.png')
			


if __name__=='__main__':
	main()