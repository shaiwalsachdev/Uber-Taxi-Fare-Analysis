import os

def main():

    pythonfilename='zmakepi_drop_profile_v2.py'
    ww = pythonfilename.split('.')
    generalLogFilename = ww[0]


    begin = 1
    window = 114

    for i in range(1,201):
        startid = begin
        endid = startid + window - 1

        logfilename = '../pi_drop_profile/logs/'+generalLogFilename+'_'+str(startid)+'_'+str(endid)+'.log'
        command = 'nohup time python -u '+pythonfilename+' '+str(startid)+' '+str(endid)+' > '+logfilename+' &'
        print command
        os.system(command)
        begin = endid+1

    logfilename = '../pi_drop_profile/logs/'+generalLogFilename+'_'+str(22801)+'_'+str(22911)+'.log'
    command = 'nohup time python -u '+pythonfilename+' '+str(22801)+' '+str(22911)+' > '+logfilename+' &'
    print command
    os.system(command)
    print "done"

if __name__=="__main__":
    main()
