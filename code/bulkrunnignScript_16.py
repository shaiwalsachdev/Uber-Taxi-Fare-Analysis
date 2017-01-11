#Run the collectdata_v5_16.py for different inputs
import os

def main():

    pythonfilename='collectdata_v5_16.py'
    ww = pythonfilename.split('.')
    generalLogFilename = ww[0]


    begin = 1
    window = 847

    for i in range(1,201):
        keyid = i
        startid = begin
        endid = startid + window - 1

        logfilename = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/16/logs/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'.log'
        command = 'nohup time python -u '+'/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' > '+logfilename+' &'
        print command
        os.system(command)
        begin = endid+1


    window = 7
    begin = 169401
    for i in range(1,10):
        keyid = i
        startid =  begin
        endid =  startid +  window - 1
        logfilename1 = '/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/16/logs/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'.log'
        command1 = 'nohup time python -u '+'/home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' > '+logfilename1+' &'
        print command1
        os.system(command1)
        begin = endid + 1


    print "done"

if __name__=="__main__":
    main()
