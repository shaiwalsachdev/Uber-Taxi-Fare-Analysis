import json

def main():

	filename = 'api_keys1.txt'
	outjsonfile = 'api_keys1.json'
	cnt = 1
	keydict = {}

	with open(filename,'r') as fin:
		for line in fin:
			line = line.strip()
			keydict[str(cnt)]=line
			cnt = cnt + 1

	print keydict

	with open(outjsonfile,'w') as jfout:
		json.dump(keydict,jfout)


	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	
	print keys['42']

	print "done"

if __name__=='__main__':
	main()