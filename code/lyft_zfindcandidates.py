#Lyft Plus,Lyft Line,Lyft vs NYC Data
import json
import gzip
import sys
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
plt.switch_backend('agg')

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
	timezone = int(sys.argv[1])

	inf = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/lyft_diff_zone'+str(timezone)+'.json.gz'
	with gzip.open(inf,'r') as jfin:
		data6 = json.load(jfin)

	
	candidates = []
	with open('/home/sankarshan/shaiwal/Uber/ByTimezone/candidates/candidates_intersection.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			candidates.append(line)
			line = infile.readline()
			
	
	diff_dict = {0:'diff_plus' , 1:'diff_line',2:'diff_normal'}
	colors = {0:'red',1:'blue',2:'green'}

	fig = plt.figure() 
	ax = fig.add_subplot(111)
	red_patch1 = mpatches.Patch(color='red', label='diff_plus')
	red_patch2 = mpatches.Patch(color='blue', label='diff_line')
	red_patch3 = mpatches.Patch(color='green', label='diff_normal')


	ax.set_ylim([0.0,1])
	for i in range(3):
		diff_lyft = dict()
		for j in candidates:
			if(data6.has_key(j)):
				xx =data6[j][diff_dict[i]] 
				if xx == 'null':
					continue;
				value = int(round(float(xx)))
				if diff_lyft.has_key(value):
					c =  diff_lyft[value]
					c = c + 1
					diff_lyft[value] = c
				else:
					diff_lyft[value] = 1
		[xaxis,yaxis] = getcdf(diff_lyft)
		print xaxis
		print yaxis
		plt.plot(xaxis,yaxis,color = colors[i])
		

	plt.legend(handles=[red_patch1,red_patch2,red_patch3],loc = 3)
	fig.suptitle('Comparison Between Lyft and NYC at Timezone'+str(timezone),fontsize = 20,fontweight='bold')
	ax.set_xlabel('Difference(Fare)',fontsize = 20,fontweight='bold')
	ax.set_ylabel('CDF',fontsize = 20,fontweight='bold')	
	#plt.tight_layout()
	fig.savefig('/home/sankarshan/shaiwal/Uber/ByTimezone/candidates/diff_lyft_'+str(timezone)+'.pdf')
			


if __name__=='__main__':
	main()