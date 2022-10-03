#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 18:11:01 2022

@author: chaojunma
"""

# The algorithm from lecture 3 

import numpy as np

first_item  = []
second_item = []

face1  = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5
house1 = ['houses1.png'] * 5 + ['houses2.png'] * 5 + ['houses3.png'] * 5 + ['houses4.png'] * 5 + ['houses5.png'] * 5

first_item.extend(face1)
first_item.extend(house1)
first_item.extend(face1)
first_item.extend(house1)

face2  = ['faces1.png', 'faces2.png','faces3.png','faces4.png','faces5.png'] * 5
house2 = ['houses1.png', 'houses2.png','houses3.png','houses4.png','houses5.png'] * 5

second_item.extend(house2)
second_item.extend(face2)
second_item.extend(house2)
second_item.extend(face2)

cues   = ['cue1'] * 50 + ['cue2'] * 50
result = list(zip(first_item,second_item,cues))

print(result)
len(result)

print('---')

np.random.shuffle(result)
print(result)



    
