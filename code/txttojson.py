import json
import gzip

def main():
	timezonedata = dict()
	outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/nyc_taxi/zone10_loc_count_avg.json'
	with open('/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/10/nyc_taxi/zone10_loc_count_avg.txt','r') as infile:
		line = infile.readline()
		
		while line:
			line = line.strip()
			details = line.split('|')
			if len(details) == 5:
				timezonedata[details[0]] = {'count':details[1],'avgdist':details[2],'avgtime':details[3],'avgfare':details[4]}
			line = infile.readline()

	with open(outjsonfile,'w') as jfout:
		json.dump(timezonedata,jfout)
	


if __name__=='__main__':
	main()



