#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:44:30 2022

@author: chaojunma
"""

# You want to tell your experiment to record participant responses.
print('---Question1---')

input_value = input('Please enter the number: ')

if(input_value == '1' or input_value == '2'):
    print('OK')
elif(input_value == '' ):
    print('subject did not respond')
    
else: print('subject pressed the wrong key')
     
print('---\n')


# Create a nested "if" statement in the above exercise. 
print('---Question2---')

input_value2 = input('Please enter the number: ')

if(input_value2 == '1' or input_value2 == '2'):
    print('OK')
    if(input_value2 == '1'):
     print('Correct!')
    if(input_value2 == '2'):
     print('Incorrect')
        
elif(input_value2 == '' ):
    print('subject did not respond')
    
else: print('subject pressed the wrong key')

print('---\n')




