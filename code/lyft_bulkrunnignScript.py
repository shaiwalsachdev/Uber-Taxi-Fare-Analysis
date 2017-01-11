import os
import sys
import time
def main():
    timezone = str(sys.argv[1])
    
    pythonfilename='lyft_collectdata_v5.py'
    ww = pythonfilename.split('.')
    generalLogFilename = ww[0]
    command = 'export http_proxy=http://10.3.100.207:8080/ && export https_proxy=http://10.3.100.207:8080/ && nohup time python -u '+'/home/sankarshan/shaiwal/Uber/ByTimezone/code/'+'lyft_generatekeyfile.py'+' > '+'/home/sankarshan/shaiwal/Uber/ByTimezone/code/key_logger.log'+'&' 
    os.system(command)

    time.sleep(600)
    begin = 1
    window = 94

    for i in range(1,201):
        keyid = i
        startid = begin
        endid = startid + window - 1

        logfilename = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/logs_lyft/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'_'+str(timezone)+'.log'
        command = 'nohup time python -u '+'/home/sankarshan/shaiwal/Uber/ByTimezone/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' '+str(timezone)+' > '+logfilename+' &'
        print command
        os.system(command)
        begin = endid+1

    window = 12
    begin = 18801
    for i in range(1,13):
        keyid = i
        startid =  begin
        endid =  startid +  window - 1
        logfilename1 = '/home/sankarshan/shaiwal/Uber/ByTimezone/'+str(timezone)+'/logs_lyft/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'_'+str(timezone)+'.log'
        command1 = 'nohup time python -u '+'/home/sankarshan/shaiwal/Uber/ByTimezone/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' '+str(timezone)+' > '+logfilename1+' &'
        print command1
        os.system(command1)
        begin = endid + 1

    print "done"

if __name__=="__main__":
    main()
