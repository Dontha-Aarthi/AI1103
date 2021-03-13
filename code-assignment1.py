# -*- coding: utf-8 -*-
"""Assignment1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17KlzHRFtf7WVUPa6vlM53hTd-caPw8_H
"""

import numpy as np
from scipy.stats import bernoulli

sample_data=10000
no_red_balls_bag1=np.size(np.nonzero(bernoulli.rvs(size=sample_data,p=3/7)))
#since there are 3 red balls and 4 black balls, Pr(E1)=3/7 -> p=3/7

no_black_balls_bag1=sample_data-no_red_balls_bag1

prob_red_bag1 = no_red_balls_bag1 / sample_data
prob_black_bag1 = no_black_balls_bag1 / sample_data

no_red_balls_bag2 = np.size(np.nonzero(bernoulli.rvs(size=sample_data,p=4/9)))
#since there are 4 red balls and 5 black balls, Pr(E1)=4/9 -> p=4/9

no_black_balls_bag2=sample_data-no_red_balls_bag2

#case1: black ball is transferred from bag 1 to bag 2
new1_no_of_red_balls_bag2 = np.size(np.nonzero(bernoulli.rvs(size=sample_data,p=4/10)))
#now one black ball is added to bag 2 so there are 4 red balls and 6 black balls, Pr(E1)=4/10 -> p=4/10

#probability of red ball being drawn from bag2 after transferring black ball from bag1 to bag2
prob_picking_red_1 = new1_no_of_red_balls_bag2/sample_data

#case2: red ball is transferred from bag 1 to bag 2
new2_no_of_red_balls_bag2 = np.size(np.nonzero(bernoulli.rvs(size=sample_data,p=5/10)))
#now one red ball is added to bag 2 so there are 5 red balls and 5 black balls, Pr(E1)=5/10 -> p=5/10

#probability of red ball being drawn from bag2 after transferring red ball from bag1 to bag2
prob_picking_red_2 = new2_no_of_red_balls_bag2/sample_data

final_result = (prob_black_bag1*prob_picking_red_1)/(prob_black_bag1*prob_picking_red_1+prob_red_bag1*prob_picking_red_2)
print("Probability that black ball is transferred from bag 1 to bag 2 if red ball is drawn from bag 2 is:{}".format(final_result))