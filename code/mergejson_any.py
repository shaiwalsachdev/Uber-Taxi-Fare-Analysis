import json
import os
import sys
import gzip
def main():

    
    timezone = int(sys.argv[1])
    total_count = int(sys.argv[2])
    total_count1 = total_count
    initials = str(timezone)+'uberprice_key'
    dict_20 = {}
    

    if total_count > 200:
        x = total_count/200
        total_count -= x*200
    
    begin = 1
    
    window = x
    for i in range(1,201):
        keyid = i
        startid = begin
        endid = startid + window - 1
        filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/uber/'+initials+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
        with gzip.open(filename,'r') as jfin:
        	keys = json.load(jfin)
		for key, value in keys.iteritems():
			dict_20[key] = json.loads(value)
        begin = endid+1


    if total_count > 50:
        x = total_count/50
        total_count -= x*50
        
        window = x
        for i in range(1,51):
            keyid = i
            startid = begin
            endid = startid + window - 1
            filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/uber/'+initials+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
            with gzip.open(filename,'r') as jfin:
            	keys = json.load(jfin)
            for key, value in keys.iteritems():
            	dict_20[key] = json.loads(value)
            begin = endid+1
    
    if total_count > 0:
        keyid = 1
        startid =  begin
        endid =  total_count1
        filename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/uber/'+initials+str(keyid)+'_sid'+str(startid)+'_eid'+str(endid)+'.json.gz'
        with gzip.open(filename,'r') as jfin:
        	keys = json.load(jfin)

        for key, value in keys.iteritems():
        	dict_20[key] = json.loads(value)
        begin = endid + 1

    outjsonfile = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/'+str(timezone)+'uberprice.json.gz'
    with gzip.open(outjsonfile,'w') as jfout:
    	json.dump(dict_20,jfout)
    
    print "done"

if __name__=="__main__":
    main()
