import os

def main():

    pythonfilename='collectdata_v5.py'
    ww = pythonfilename.split('.')
    generalLogFilename = ww[0]


    begin = 1
    window = 50

    for i in range(1,201):
        keyid = i
        startid = begin
        endid = startid + window - 1

        logfilename = '/home/bt2/14CS10061/shaiwal/Uber/logs/'+generalLogFilename+'_'+str(keyid)+'_'+str(startid)+'_'+str(endid)+'.log'
        command = 'nohup time python -u '+'/home/bt2/14CS10061/shaiwal/Uber/code/'+pythonfilename+' '+str(keyid)+' '+str(startid)+' '+str(endid)+' > '+logfilename+' &'
        print command
        os.system(command)
        begin = endid+1


    print "done"

if __name__=="__main__":
    main()
