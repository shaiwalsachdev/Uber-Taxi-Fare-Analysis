import json

def main():

	filename = '../pi_drop_profile/dropoff.txt'
	outjsonfile = '../pi_drop_profile/dropoff.json'
	cnt = 1
	keydict = {}

	with open(filename,'r') as fin:
		for line in fin:
			line = line.strip()
			keydict[line]= 1
			cnt = cnt + 1

	print keydict

	with open(outjsonfile,'w') as jfout:
		json.dump(keydict,jfout)


	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	print keys['40.725382_-74.000101']
	print "done"

if __name__=='__main__':
	main()