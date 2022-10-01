#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:42:02 2022

@author: chaojunma
"""

# Question 1

import numpy as np;

num_list = [1,2,3]
print(num_list * 2)

num_arr = np.array([1,2,3])
print(num_arr * 2)

# Question 2

strlist = ['do','re','mi','fa']


# case 1 : ['dodo','rere','mimi','fafa'] 

print([strlist[0] * 2, strlist[1] * 2, strlist[2] * 2, strlist[3] * 2])

# case 2: ['do','re','mi','fa','do','re','mi','fa'] 

print(strlist * 2)

# case 3: ['do','do','re','re','mi','mi','fa','fa'] 

print([strlist[0],strlist[0],
       strlist[1],strlist[1],
       strlist[2],strlist[2],
       strlist[3],strlist[3]])

# case 4: [['do','do'],['re','re'],['mi','mi'],['fa','fa']]

print([
       [strlist[0],strlist[0]],
       [strlist[1],strlist[1]],
       [strlist[2],strlist[2]],
       [strlist[3],strlist[3]]
       
       ])