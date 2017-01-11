import json
import gzip
import sqlite3
import pandas as pd
from bisect import bisect_left
import time
import numpy as np
import os
import sys
import pandas as pd

#test code
	
def main():

    idlow = int(sys.argv[1])
    idhi = int(sys.argv[2])

    conread = sqlite3.connect("../output/testlocation10000.sqlite")

    with conread:
        
        Q = 'select * from locind where id >={qidlow} and id <={qidhi}'\
        .format(qidlow=idlow,qidhi=idhi)
           
        df = pd.read_sql_query(Q,conread)

#    print "\tdf created"
#    print len(df)
    loclist = list(df['location'])
    print loclist

    print "done"


if __name__=="__main__":
    main()

    
  