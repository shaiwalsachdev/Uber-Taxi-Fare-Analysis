import sys
import gzip
import json
def main():
	cluster_no = int(sys.argv[1])
	
	

	#CSV FILE With latitudes and longitudes
	PATH = "cluster.json.gz"
	with gzip.open(PATH,'r') as jfin:
		keys = json.load(jfin)
	

	#Result string
	result = ""

	lineno  = 0
	PATH = "marker.html"
	with open(PATH,'r') as infile:
		line = infile.readline()
		
		
		
		while line:
			line = line.strip()
			result = result + line + "\n"

			if line == "var locations = [":
				points = ""
				count = 0
				locations = list(keys[str(cluster_no)])

				for l in locations:

					line = l.split('_')

					lat = line[0]
					longi = line[1]
					count =  count + 1
					#print row
					add = "["+"\'Location"+str(count)+"\'" +", "+str(lat) + ", " + str(longi) + "]"
					points = points + add + ","
					

				points = points[:-1]

				result = result + points+"\n"

				while not line =="];":
					line = infile.readline().strip()
				result = result + line
			
			line = infile.readline()
			lineno = lineno + 1


	PATH = "mark_out"+str(cluster_no)+".html"
	with open(PATH, 'w')  as outputfile:
		for i in result:
			outputfile. write(i) 
			

if __name__=='__main__':
	main()