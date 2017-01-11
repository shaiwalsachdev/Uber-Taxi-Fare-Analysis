#Importing Packages
import requests
import json
import sys
import pandas as pd
import numpy as np
import gzip

#For parallel processing
from joblib import Parallel, delayed
import multiprocessing
import time
from requests.exceptions import ConnectionError
#Function to get the price giving input the parameters
#Run the function for each line of input file that is for each of source destination co-ordinates given
#lat_long is a list of the four parameters start_latitude,start_longitude,end_latitude,end_longitude
def uber_getprice(server_token,line):
	lat_long = line.split('_')
	url = 'https://api.uber.com/v1/estimates/price'
	
	parameters = {
	'server_token': server_token,
	'start_latitude': lat_long[0],
	'start_longitude': lat_long[1],
	'end_latitude': lat_long[2],
	'end_longitude': lat_long[3],
	}
	
	#GET the url
	try:
		response = requests.get(url,params=parameters)
	except ConnectionError: 
		time.sleep(2)
		response = requests.get(url,params=parameters)
	
	#print response.url
	#response data in json
	#data = response.json()
	return response.text
	#return data.text

#The Time Estimates endpoint returns ETAs for all products currently available at a given location 
#lat_long take start_latitude and start_longitude as parameters
def uber_gettime(lat_long,id):
	
	url = 'https://api.uber.com/v1/estimates/time'
	
	server_token = []
	server_token.append('FhVyrIYw7Qs2YFbJlrowAgPGQx9QXMWixndjUyl3')
	server_token.append('DOe7jlbzn201QZY4wDDt5zBhlWg73KvwNs4u2yQH')


	parameters = {
	'server_token': server_token[id],
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


	#Store all the server tokens at one place
	server_token = []

	#shaiwalsachdev@gmail.com
	server_token.append('FhVyrIYw7Qs2YFbJlrowAgPGQx9QXMWixndjUyl3')
	
	server_token.append('DOe7jlbzn201QZY4wDDt5zBhlWg73KvwNs4u2yQH')
	server_token.append('iPRJZN0jvzFQAhteRd1Xlvc1Tdl1Ctcl5BAMG-IG')
	server_token.append('r6FERLboXcWCMFZr5szmi7DY4-F_TuJdedHrqk2F')
	server_token.append('8zd_keRpYp46Iy8P0wj6DFOd3YkdpSAnmJdfx9cN')


	#asabhi786@gmail.com
	server_token.append('eWLi0qRBmcrpKRLDfbmCOGmn9mtj5-uqr22vR-wm')
	server_token.append('z0vUseQjbB6zJYj7WABx8lX5feKK79JRZoDxQ619')
	server_token.append('qH8YfxWwn0zP2-g1NVLr9KjpVfmgqEujwgYcdxH')
	server_token.append('PBeQHHYS1KA7qdrM2g7PGRAz8vwmCVzL_l_YzVvt')
	server_token.append('Vpo4ds7vjd4T5cmcirFm9qJOzX6_8Jy78lE-d6o-')

	#anurag4446@gmail.com
	server_token.append('4mI3Ua6arkCguvJMCAl1pWRViJ1immeDeZCPsgjj')
	server_token.append('0Iv760dUAj_qVXPAPJKJLUo2eBD68p9nlmyk3GHk')
	server_token.append('6rxm-H2o4Q6jpGVh0q8eY2VuU06z5g4qejXC4DmY')
	server_token.append('Xrly75CQGoxHEhnmHSqIilXe157dpQp85onibbmM')
	server_token.append('RWM674gvE_fvNOty0-f5ul-DdRjCM3Y9SNUlcvgK')

	#iit2013196@iiita.ac.in
	server_token.append('TnwzsRcel9TQNhPE308byl70JeWNGFZeu-qUlo0f')
	server_token.append('40Qk7IcgF6GxfVUChwHdTUhL0Xk5n2LMO8BjjWLi')
	server_token.append('MVtb7LhAYwQvpNUaUMKs1ix-Gl18QLiylijVl0Cn')
	server_token.append('8ffvBua44iMMAWdygR-C2sFDTTy8GhsKbTVIDf2z')
	server_token.append('NVVGcCMvjOQQsO4KoGKNtkKR7pk3jP1-DmhKFloq')

	#gshantanu3@gmail.com
	server_token.append('qkzy_mSAyV8G1ePXhEzw6M33Ow2IgkLr0nE37JZe')
	server_token.append('LdxAAZc3Qti3K-seVkxNMujeO_dmSoh6DfXRUZYv')
	server_token.append('7Z0G0rfuTCfsyV2b4bcVxk6pIqnNF9D2SCy2OUxs')
	server_token.append('YGeiLBz1HeC7xwg9ERLySyGfKP0TzHaOPFTtBcg7')
	server_token.append('uVfY9yYh6w36lIHcsBAJG2rPVuFvMekHp-c9I2MY')

	#iit2013131@iiita.ac.in
	server_token.append('lKhJv2HFlAMzv0LGVYDRVoAf5721_P90caav_p6Y')
	server_token.append('xGQGjso3CBx2U2i_p_dRfZ2TCvf-OBCb4nnzetqk')
	server_token.append('NFv1q8tdJ-1uYl2axI2unqwqVGDtXX7aZUAHQGUs')
	server_token.append('XYlxiYItu1esDGgI8zwntys5n0aVHBqM5-YhuUlO')
	server_token.append('TQQYUCFydl4Vi1IcH2TG-VX-Dxpt4ApoCKUYuggW')

	#akshaykarnwal3@gmail.com
	server_token.append('u8tIzS2XTGmHibDmMd5W2bY8_YiTAxN4xC9F-nry')
	server_token.append('TOjXTZShM_Dokf3O6Fs6a7efHGLr2CeQDUjrNmUT')
	server_token.append('Ovz76NuqFZkNjcsBJMp7bh9tsi72UUdGPyCDLbPQ')
	server_token.append('hIBhdhgzIsYnkD9CNAGl0DNPYpkg5pNPMaP1h6gz')
	server_token.append('Dcq8IXvQtMp2HHjjCObbjjATYssuC-0cP3TjsIGM')

	#kamalsachdevay@gmail.com
	server_token.append('mc6g23_VmPnqkG1v9zmFp8Ypu0g5RHFSbDv3CjDy')
	server_token.append('eucbWqJR33fBunGtOziPb0mq8L4rP77XWsviU8I5')
	server_token.append('jHiN7ZoFMKKWzUyDe0sb06-olrcZJ-6iQd_ngnTa')
	server_token.append('098l592sFzgESVb00b4GIafxtaaY10Im6jPyJr1i')
	server_token.append('wiakfuckbwnrh8t7i9BHDeuiP5BM5w-Nsi876QDF')

	#aishwarya2612@gmail.com
	server_token.append('1G9pnA7cUL3GWGpNZuc4qt1OhFo5sLKHP9po9Kha')
	server_token.append('93P9s2QCoSJLqbAkbFxQm5TCaOYuslWAp3jXKrdg')
	server_token.append('wZo4KtKE36sv34g45oX4XNvlNa1MlGlV2Lo0NT0_')
	server_token.append('CVXHJEkRoP8hV14elor2cbyx4dgdQOUTv6YWd_vR')
	server_token.append('CdHMnvo4Qz0sPRYMIRhdP3arf0oRvCeEhltGEOVN')

	#shaiwalcoilbooks@yahoo.in
	server_token.append('BMwll_oPVcZKVtPDVimQN00osH2QWGJCYB9Fu9HH')
	server_token.append('ZvsK0EW-B0MgzpNGiTwXWupqMFvt5kxsUfej7akv')
	server_token.append('1fWez3_MGeLKmi5dqjwxMBdgvQs5c0LhpFoIpvbY')
	server_token.append('tWDtxBm7Eyq9nSdQgUFqEGg--4IQgMVl0Vkkpri2')
	server_token.append('jXQSROgKN28BAhID4lTaLk17fhZNQ7TD6Qr_0gwc')
	
	#Store all the json responses in the form of text
	output = [] #For uber price
	output1 = [] #For uber time
	
	#1st line
	line = inputfile.readline()
	i = 0
	counter = 0
	input_list = []
	
	while line:
		
		if i == 10000:
			break

		#Check unnecessary lines
		lat_long = line.split('_')
		if len(lat_long) < 4 :
			line = inputfile.readline()
			continue;
		
		i = i + 1
		input_list.append(line)
		counter = counter + 1
		if counter < 50:
			line = inputfile.readline()
			continue;
		else:
			num_cores = multiprocessing.cpu_count()
			#print num_cores
			results = Parallel(n_jobs=num_cores)(delayed(uber_getprice)(server_token[i],input_list[i]) for i in range(50))
			output.append(results)
			print len(results)
			input_list = []
			line = inputfile.readline()
			counter = 0

			

		#output.append(uber_getprice(server_token,line,id))
		
		#output1.append(uber_gettime(lat_long),1)
		#output2.append(ola_getprice(lat_long) + "\n")
		
		
		

	inputfile.close()


	#print json.loads(output[0])['prices'][0]['estimate']
	
	#Write output now
	with gzip.open('../output/estimatespricesjson1.txt.gz', 'w')  as outputfile:
		for i in output:
			for j in range(50):
				outputfile. write(i[j]) 
				outputfile. write(' \n')

	with gzip.open('../output/estimatestimejson1.txt.gz', 'w')  as outputfile1:
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