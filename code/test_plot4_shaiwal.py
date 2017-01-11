import pandas as pd
import numpy as np

import pylab
import matplotlib

import sys

def main():

    font = {'weight' : 'bold'}                                                  
    matplotlib.rc('font', **font)

#    filename = 'PD2_S1_W_filtered_Outliar.txt'
    
    param = str(sys.argv[1])
    fileW = 'coefficient_of_variation_allmonths_W.txt'
    fileNW = 'coefficient_of_variation_allmonths_NW.txt'

    dfw = pd.read_csv(fileW,sep='\t',dtype=object)
    dfnw = pd.read_csv(fileNW,sep='\t',dtype=object)

    col = ['timezone','CV']
    dfw.columns = col
    dfnw.columns = col

    dfw[['timezone']] = dfw[['timezone']].astype(long)
    dfw[['CV']] = dfw[['CV']].astype(float)

    dfnw[['timezone']] = dfnw[['timezone']].astype(long)
    dfnw[['CV']] = dfnw[['CV']].astype(float)

#    print df
    n_groups = 24
    index = np.arange(24)
    
    tz = range(0,24,1)
    
    ttw = list(dfw['CV'])
    cvw = [round(x,2) for x in ttw]

    ttnw = list(dfnw['CV'])
    cvnw = [round(x,2) for x in ttnw]

    opacity = 0.1
    barwidth = 0.3


    #plotting begins:
    fig = pylab.figure()
    ax = fig.add_subplot(111)
    bp = ax.bar(index,dfw['CV'],barwidth,color='midnightblue',alpha=opacity,label='weekdays') #sym="" to off the outliers
    bp = ax.bar(index+barwidth,dfnw['CV'],barwidth,color='coral',alpha=opacity,label='weekends')


    '''color=cs, alpha=0.8
    for whisker in bp['whiskers']:
        whisker.set(color='grey',linewidth=2)

    for cap in bp['caps']:
        cap.set(linewidth=2)

    for median in bp['medians']:
        median.set(color='red',linewidth=2)
    '''

    pylab.legend(loc=2)
    ax.set_xlabel('Hours of the day',fontweight='bold')#
    ax.set_ylabel('Coefficienf of variation',fontweight='bold') 
#    ax.set_xticklabels(['0', '', '2', '','4','','6','','8','','10','','12','','14','','16','','18','','20','','22',''])

    ax.set_xlim([0,24])
    #removing xtick
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(20) 


    pylab.tight_layout() 
    pylab.savefig('coefficient_of_variation_allmonths_11.eps',)
 #   pylab.show()

#    print ss
#    print df
#    print nonlisted
#    print org_tz

#    print df
    
    print "done"


if __name__=="__main__":
    main()
