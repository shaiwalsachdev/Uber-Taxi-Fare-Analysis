import sqlite3
import csv
import time

def getchunkCSV(data,rows=10000 ):
    """Divide the data into <rows> rows each"""

    for i in xrange(0, len(data), rows):
        yield data[i:i+rows]


def main():
    t = time.time()
    filename = '../output/PD_AVGDIST_0.1_2.txt'
    conn = sqlite3.connect("../output/locationListIndex_new.sqlite")

    conn.text_factory = str
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS locind;")
    cur.execute('create table locind (location text primary key,id integer)')

    csvData = csv.reader(open(filename,'r'))
    divData = getchunkCSV(list(csvData))
    cnt = 1
    for chunk in divData:
        cur.execute('BEGIN TRANSACTION')
        for item in chunk:
            f1 = item[0].strip()
            cur.execute('INSERT OR IGNORE INTO locind (location,id) VALUES (?,?)',(f1,cnt))
            cnt = cnt + 1
            print cnt

        conn.commit()

    print "\n Tome taken: %.3f sec" %(time.time()-t)

    print "done"

if __name__=="__main__":
    main()




