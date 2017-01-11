#Locally Weighted Regression fro Input is of 1 dimension
import numpy as np
import pandas as pd 
import math

import numpy as np

def lwr_predict(x,y,datapoint):
    c = 1.0
    weights = []
    for i in range(len(x)):
        xx = float(abs(x[i]-datapoint)*abs(x[i]-datapoint))
        yy = math.exp((xx)/(-2.0* c**2))
        weights.append(yy)

    summ = 0
    for i in range(len(weights)):
        summ = summ + x[i]*x[i]*weights[i]

    summ = 1.0/summ 

    summ1 = 0
    for i in range(len(weights)):
        summ1 = summ1 + x[i]*y[i]*weights[i]

    beta = summ*summ1
    return beta*datapoint

def main():
    data = pd.read_csv('../estimator/candidates.csv')
    features = list(data.popularity)
    target = list(data.surcharge)
    datapoint = 878.754481968
    print lwr_predict(features,target,datapoint)
    
if __name__=='__main__':
    main()