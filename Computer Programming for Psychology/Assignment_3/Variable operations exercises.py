#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:40:23 2022

@author: chaojunma
"""

### init variables

sub_code = 'sub'
subnr_int = 2
subnr_str = '2'

### Question 1

try:
    print(sub_code+subnr_int)
except Exception as e:
    print(e.args)

print(sub_code+subnr_str)


### Question 2


### case 1 sub 2
print(sub_code + ' '+ subnr_str)

### case 2 sub 222
print(sub_code + ' '+ (subnr_str * 3))

### case 3 sub2sub2sub2
print((sub_code+subnr_str)* 3)

### case 4 subsubsub222
print((sub_code * 3) + (subnr_str * 3))

S