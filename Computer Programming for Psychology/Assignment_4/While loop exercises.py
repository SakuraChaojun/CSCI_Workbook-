#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 00:22:24 2022

@author: chaojunma
"""

"""
Create a while loop of 20 iterations that prints 
"image1.png" for the first 10 iterations, and "image2.png" for the next 10 iterations.

Alternative, we can apply the recursion function 
def image_cycle(n):
    if (n < 10):
     print('image1.png')
     return n + image_cycle(n+1)
     
    elif (n>=10 and n<20):
     print('image2.png')
     return n + image_cycle(n+1)
    else:
        return 0

image_cycle(0)

"""
# Question 1

flag = 0

while(flag < 20 ):
    
    while(flag < 10):
      print('image1.png')
      flag = flag + 1
      
    while(flag < 20):
        print('image2.png')
        flag = flag + 1
        

#Create a while loop that shows an image until the participant makes a response of 1 or 2. 
#Run it a few times to make sure it works the way you expect.
print('---\n')

import random

response = ''

while(True):
    print('This is an image\n')
    response = random.randint(0,10)
    print('The response is %i'%response  )
    if response == 1 or response == 2:
        break

#Create a failsafe that terminates the previous while loop after 5 iterations 
#if one of the valid responses (1,2) have not been made in that time.

print('---\n')

response = ''
failsafe = 0

while(True):
    
    print('This is an image\n')
    response = random.randint(0,10)
    print('The response is %i'%response)
    
    failsafe = failsafe + 1 
    
    if response == 1 or response == 2 or failsafe == 5:
        if(failsafe == 5):
            print('failsafe work !')
        break




















