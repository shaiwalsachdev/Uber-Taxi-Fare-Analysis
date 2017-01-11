#Importing Packages
import requests
import json
import sys
import pandas as pd
import numpy as np
import gzip
#Function to get the price giving input the parameters
#Run the function for each line of input file that is for each of source destination co-ordinates given
#lat_long is a list of the four parameters start_latitude,start_longitude,end_latitude,end_longitude
def ola_getprice(lat_long):
	url = 'https://devapi.olacabs.com/v1/products'
	headers = {'X-APP-TOKEN': '39404d8937d5433b9d36d490da83fcd9'}
	parameters = {
	'pickup_lat': lat_long[0],
	'pickup_lng': lat_long[1],
	'drop_lat': lat_long[2],
	'drop_lng': lat_long[3],
	}
	
	#GET the url
	response = requests.get(url,params=parameters,headers=headers)
	
	print response.url
	#response data in json
	#data = response.json()
	return response.text
	#return data.text


#Function to get the price giving input the parameters
#Run the function for each line of input file that is for each of source destination co-ordinates given
#lat_long is a list of the four parameters start_latitude,start_longitude,end_latitude,end_longitude
def uber_getprice(lat_long):
	
	url = 'https://api.uber.com/v1/estimates/price'
	
	parameters = {
	'server_token': 'DOe7jlbzn201QZY4wDDt5zBhlWg73KvwNs4u2yQH',
	'start_latitude': lat_long[0],
	'start_longitude': lat_long[1],
	'end_latitude': lat_long[2],
	'end_longitude': lat_long[3],
	}
	
	#GET the url
	response = requests.get(url,params=parameters)
	
	#print response.url
	#response data in json
	#data = response.json()
	return response.text
	#return data.text

#The Time Estimates endpoint returns ETAs for all products currently available at a given location 
#lat_long take start_latitude and start_longitude as parameters
def uber_gettime(lat_long):
	
	url = 'https://api.uber.com/v1/estimates/time'
	
	parameters = {
	'server_token': 'DOe7jlbzn201QZY4wDDt5zBhlWg73KvwNs4u2yQH',
	'start_latitude': lat_long[0],
	'start_longitude': lat_long[1],
	}
	
	#GET the url
	response = requests.get(url,params=parameters)
	
	#print response.url
	#response data in json
	#data = response.json()
	return response.text
	#return data.text


#Function to read data and generate the json response file
def read_gentxt():
	#Read the given file line by line
	inputfile = open('../dataset/testlocation10000.txt', "r")

	#Store all the json responses in the form of text
	output = [] #For uber price
	output1 = [] #For uber time
	#output2 = [] #For ola price
	#1st line
	line = inputfile.readline()
	i = 0
	while line:
		#SPLIT The parameters concatenated by _
		if i == 200:
			break
		lat_long = line.split('_')
		if len(lat_long) < 4 :
			line = inputfile.readline()
			continue;

		output.append(uber_getprice(lat_long))
		output1.append(uber_gettime(lat_long))
		#output2.append(ola_getprice(lat_long) + "\n")

		line = inputfile.readline()
		i = i + 1

	inputfile.close()


	#print json.loads(output[0])['prices'][0]['estimate']
	
	#Write output now
	with gzip.open('../output/estimatespricesjson.txt.gz', 'w')  as outputfile:
		for i in output:
			outputfile. write(i) 
			outputfile. write(' \n')

	with gzip.open('../output/estimatestimejson.txt.gz', 'w')  as outputfile1:
		for i in output1:
			outputfile1. write(i) 
			outputfile1. write(' \n')
	
#Now Generate the data showing the start_lat,start_long,end_lat,end_long,price_estimate,duration,distance,time_estimate_for_start

def visualize():
	data = np.zeros(shape = (40,8),dtype="S50")

	#Get Coordinates
	inputfile = open('nyclocation4UBER.txt', "r")
	line = inputfile.readline()
	i = 0
	while line:
		#SPLIT The parameters concatenated by _
		lat_long = line.split('_')
		if len(lat_long) < 4 :
			line = inputfile.readline()
			continue;
		data[i][0] = lat_long[0]
		data[i][1] = lat_long[1]
		data[i][2] = lat_long[2]
		data[i][3] = lat_long[3]
		line = inputfile.readline()
		i = i + 1
	inputfile.close()


	#Get price_estimate and duration and distance
	#print json.loads(output[0])['prices'][0]['estimate']
	inputfile = open('estimatespricesjson.txt', "r")
	line = inputfile.readline()
	i = 0
	while line:
		#SPLIT The parameters concatenated by _
		txttojson = json.loads(line)
		data[i][4] = txttojson['prices'][0]['estimate']
		data[i][5] = txttojson['prices'][0]['duration']
		data[i][6] = txttojson['prices'][0]['distance']
		line = inputfile.readline()
		i = i + 1
	inputfile.close()

	#Get time estimate for start coordinate only
	#print json.loads(output[0])['prices'][0]['estimate']
	inputfile = open('estimatestimejson.txt', "r")
	line = inputfile.readline()
	i = 0
	while line:
		#SPLIT The parameters concatenated by _
		txttojson = json.loads(line)
		data[i][7] = txttojson['times'][0]['estimate']
		line = inputfile.readline()
		i = i + 1
	inputfile.close()

	make_dataframe = pd.DataFrame({'start_lat':data[:,0],'start_long':data[:,1],'end_lat':data[:,2],'end_long':data[:,3],'price_estimate':data[:,4],'duration':data[:,5],'distance':data[:,6],'time_estimate_for_start':data[:,7]})
	print make_dataframe.to_html()






#Read and generate the json response file
read_gentxt()

#Visualize the data make a dataframe
#visualize()