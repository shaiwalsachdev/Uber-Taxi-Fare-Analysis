
#Lyft Plus,Lyft Line,Lyft
import json
import gzip
import sys

def main():
	timezone = int(sys.argv[1])
	injson = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/nyc_taxi/'+'zone'+str(timezone)+'_loc_count_avg.json'
	with open(injson,'r') as jfin:
		nyc = json.load(jfin)


	injson1 = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/'+str(timezone)+'lyftprice.json.gz'
	with gzip.open(injson1,'r') as jfin:
		lyft = json.load(jfin)

	outjsonfile = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/lyft_diff_zone'+str(timezone)+'.json.gz'

	distribution = dict()
	with open('/home/sankarshan/shaiwal/Uber/ByTimezone/candidates/candidates_intersection.txt','r') as infile:
		line = infile.readline()
		while line:
			line = line.strip()
			if line == '':
				continue
			nyc_fare = float(nyc[line]['avgfare'])
			c = 0
			c1 = 0
			c2 = 0
			if(lyft[line].has_key('cost_estimates')):
				for i in lyft[line]['cost_estimates']:
					if i['display_name'] == 'Lyft Plus':
						c = 1
						lyft_plus = (float(i['estimated_cost_cents_max']) +float(i['estimated_cost_cents_min']))/200 - nyc_fare;

					if i['display_name'] == 'Lyft Line':
						c1 = 1
						lyft_line = (float(i['estimated_cost_cents_max']) +float(i['estimated_cost_cents_min']))/200 - nyc_fare;
					if i['display_name'] == 'Lyft':
						c2 = 1
						lyft_normal = (float(i['estimated_cost_cents_max']) +float(i['estimated_cost_cents_min']))/200 - nyc_fare;
				

			if c == 0:
				lyft_plus = 'null'
			if c1 == 0:
				lyft_line = 'null'
			if c2 == 0:
				lyft_normal = 'null'

			distribution[line] = {'diff_plus':lyft_plus , 'diff_line':lyft_line,'diff_normal':lyft_normal}
			line = infile.readline()

	with gzip.open(outjsonfile,'w') as jfout:
		json.dump(distribution,jfout)
			




if __name__=='__main__':
	main()