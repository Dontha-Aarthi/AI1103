# -*- coding: utf-8 -*-
"""assignment3(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13SiKFG-uU5iyrPtfbxEbgSXGFtccQp4h
"""

from scipy.stats import poisson
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sn
import xlrd
import scipy as sp

_lambda=1
simlen=100000
count_2=0
count_3=0
count_4=0
r=poisson.rvs(_lambda,size=simlen)
for i in range(0,simlen):
  if(r[i]==2):
    count_2=count_2+1
  if(r[i]==3):
    count_3=count_3+1
  if(r[i]==4):
    count_4=count_4+1

cdf=[poisson.cdf(0,_lambda), poisson.cdf(1,_lambda), poisson.cdf(2,_lambda), poisson.cdf(3,_lambda), poisson.cdf(4,_lambda) ]

X = [0,1,2,3,4]

plt.xlim([0,4])
plt.ylim([0,2])
plt.title('CDF')
plt.xlabel('X')
plt.ylabel('F(X)')
markerline, stemlines, baseline = plt.stem(X,cdf, '-')
plt.show()

prob_2=count_2/simlen
prob_3=count_3/simlen
prob_4=count_4/simlen

prob_S=prob_2+prob_3+prob_4

prob_T=poisson.cdf(4,_lambda)-poisson.cdf(1,_lambda)


data1 = {'theoritical probability':prob_T, 'simulated probability':prob_S}
prob_type = list(data1.keys())
prob = list(data1.values())
  
fig = plt.figure(figsize = (6, 4))
 
# creating the bar plot
plt.bar(prob_type,prob, color ='violet',width = 0.1)
plt.xlabel("type of probability")
plt.ylabel("probability")
plt.show()