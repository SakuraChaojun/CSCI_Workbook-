#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 23:49:03 2022

@author: chaojunma
"""

#Create a for loop that prints each letter without writing out all of the print statements manually.

name = ['C','H','A','O','J','U','N']

for char in name:
    print(char)

# Add an index counter and modify your loop to print the index number after each letter

print('---\n')
flag = -1

for char in name:
    flag = flag +1
    print(f'{char} index is {flag}')

# Create a list of names "Amy","Rory", and "River". 

print('---\n')

list_name = ['Amy','Rory','River']

for name in list_name:
    print(name)
    for char in name:
        print(char)
    print('\n')    
    
# Add an index counter that gives the index of each letter for each name.
print('---\n')

for name in list_name:
    print(name+'\n')
    counter = -1
    for char in name:
        counter = counter + 1
        print(char)
        print("The index of this char is  %i" %counter)
    print('\n')
    
