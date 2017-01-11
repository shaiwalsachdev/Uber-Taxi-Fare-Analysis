import time
import os
import json
import requests

#send request to generate tokens and write them to file and then we will read from that file
def gettokenintofile(i,cid,csecret):
	outf = '/home/sankarshan/shaiwal/Uber/ByTimezone/code/lyft_tokens/token'+str(i)+'.json'
	auth = cid+':'+csecret
	
	command = 'curl -X POST -H \"Content-Type: application/json\" --user \"'+cid+':'+csecret+"\" -d '{\"grant_type\": \"client_credentials\", \"scope\": \"public\"}' 'https://api.lyft.com/oauth/token' "+ "> "+outf
	#print command
	os.system(command)
	time.sleep(1)
	with open(outf,'r') as jfin:
		keys = json.load(jfin)


	return keys['access_token']


	
def main():
	with open('/home/sankarshan/shaiwal/Uber/ByTimezone/code/lyft_client_id.json','r') as jfin:
		client_id = json.load(jfin)
	with open('/home/sankarshan/shaiwal/Uber/ByTimezone/code/lyft_client_secret.json','r') as jfin:
		client_secret = json.load(jfin)

	acctokens = dict()
	for i in range(1,101):
		tt = gettokenintofile(i,client_id[str(i)],client_secret[str(i)])
		acctokens[str(i)]=tt

	for i in range(101,201):
		acctokens[str(i)]=acctokens[str(i-100)]

	outjsonfile = '/home/sankarshan/shaiwal/Uber/ByTimezone/code/lyft_client_id.json/lyft_keys.json'
	with open(outjsonfile,'w') as jfout:
		json.dump(acctokens,jfout)
	


if __name__=="__main__":
    main()

