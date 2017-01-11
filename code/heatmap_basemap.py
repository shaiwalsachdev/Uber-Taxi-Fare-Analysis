import pandas as pd 
import csv
import json
import gzip
import sys
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.switch_backend('agg')
def main():
	timezone = int(sys.argv[1])
	uber_service = int(sys.argv[2])
	datainput = pd.read_csv("../estimator/"+str(timezone)+"_"+str(uber_service)+"lat_long_popularity_surcharge.csv")
	
	lat = list(datainput['latitude'])
	lon = list(datainput['longitude'])


	m = Basemap(projection='mill',llcrnrlat=min(lat),urcrnrlat=max(lat),llcrnrlon=min(lon),urcrnrlon=max(lon),resolution='c')
	m.drawcoastlines()
	m.drawcountries()
	m.drawstates()
	m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
	m.drawmapboundary(fill_color='#FFFFFF')

	x,y = m(lon,lat)
	m.plot(x,y,'ro',markersize=4,alpha=.5)

	plt.title('Geo Plotting')
	plt.savefig("g.pdf")


if __name__=='__main__':
	main()