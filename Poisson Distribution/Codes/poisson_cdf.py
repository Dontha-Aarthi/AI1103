from scipy.stats import poisson
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sn
import xlrd
import scipy as sp
import math

_lambda=7
simlen=100000
r=poisson.rvs(_lambda,size=simlen)
sim_cdf=[]

for k in range(0,11):
  sim_cdf.append(poisson.cdf(k,_lambda))

X = [0,1,2,3,4,5,6,7,8,9,10]

plt.xlim([0,10])
plt.ylim([0,1])
plt.title('Cumulative Distribution Function ($\lambda$=3)')
plt.xlabel('k')
plt.ylabel('F(k,$\lambda$)')
markerline, stemlines, baseline = plt.stem(X,sim_cdf, '-')
plt.show()