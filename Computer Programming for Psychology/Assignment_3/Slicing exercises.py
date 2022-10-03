#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 01:00:41 2022

@author: chaojunma
"""

# Create a list of numbers 0-100 called "list100".
list100 = list(range(101))
print(list100)
print('---')

# Using slicing, print the first 10 numbers in the list.
print(list100[:10])
print('---')

# Using slicing, print all the odd numbers in the list backwards.
print(list100[99:0:-2])
print('---')

# Using slicing, print the last four numbers in the list backwards.
print(list100[100:96:-1])
print('---')

# Are the 40th-44th numbers in the list equal to integers 39-43? Show the Boolean operation you would use to determine the truth value.
print(list100[39:44] == [39,40,41,42,43])
print('---')