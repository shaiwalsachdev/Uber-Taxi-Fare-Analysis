#Run the collectdata_v5_any.py for different inputs
import os
import sys
def main():

    pythonfilename='collectdata_v5_any.py'
    ww = pythonfilename.split('.')
    generalLogFilename = ww[0]
    timezone = int(sys.argv[1])
    total_count = int(sys.argv[2])
    total_count1 = total_count

    

    if total_count > 200:
        x = total_count/200
        total_count -= x*200
    
    begin = 1
    
    window = x
    for i in range(1,201):
        keyid = i
        startid = begin
        endid = startid + window - 1
        logfilename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/logs/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'.log'
        command = 'nohup time python -u '+'/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' '+str(timezone)+' > '+logfilename+' &'
        print command
        os.system(command)
        begin = endid+1


    if total_count > 50:
        x = total_count/50
        total_count -= x*50
        
        window = x
        for i in range(1,51):
            keyid = i
            startid = begin
            endid = startid + window - 1
            logfilename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/logs/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'.log'
            command = 'nohup time python -u '+'/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' '+str(timezone)+' > '+logfilename+' &'
            print command
            os.system(command)
            begin = endid+1
    
    if total_count > 0:
        keyid = 1
        startid =  begin
        endid =  total_count1
        logfilename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/'+str(timezone)+'/logs/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'.log'
        command = 'nohup time python -u '+'/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' '+str(timezone)+' > '+logfilename+' &'
        print command
        os.system(command)
        begin = endid + 1

    
    print "done"

if __name__=="__main__":
    main()
