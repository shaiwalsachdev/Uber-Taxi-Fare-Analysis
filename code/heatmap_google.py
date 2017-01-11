import sys
import pandas as pd
def main():
	timezone = int(sys.argv[1])
	uber_service = int(sys.argv[2])
	choice = int(sys.argv[3])
	#0 for populairty heatmap
	#1 for surcharge hetmap

	#CSV FILE TO MAKE HEATMAP OF
	PATH = "../estimator/"+str(timezone)+"_"+str(uber_service)+"lat_long_popularity_surcharge.csv"
	data = pd.read_csv(PATH)
	

	#Result string
	result = ""

	lineno  = 0
	PATH = "../plots/test.html"
	with open(PATH,'r') as infile:
		line = infile.readline()
		
		
		
		while line:
			line = line.strip()
			result = result + line + "\n"

			if line == "var taxiData = [":
				points = ""
				count = 0
				for index,row in data.iterrows():
					count =  count + 1
					#print row
					if choice == 0:
						add = "{location:new google.maps.LatLng(" + str(row['latitude']) + ", " + str(row['longitude']) + "),weight:" + str(row['popularity']) + "}"
					else:
						add = "{location:new google.maps.LatLng(" + str(row['latitude']) + ", " + str(row['longitude']) + "),weight:" + str(row['surcharge']) + "}"
					points = points + add + ","
					if count == 5:
						break

				points = points[:-1]

				result = result + points+"\n"

				while not line =="];":
					line = infile.readline().strip()
				result = result + line
			
			line = infile.readline()
			lineno = lineno + 1


	PATH = "../plots/"+str(timezone)+"_"+str(uber_service)+"_"+str(choice)+"heatmap.html"
	with open(PATH, 'w')  as outputfile:
		for i in result:
			outputfile. write(i) 
			

if __name__=='__main__':
	main()