#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 23:46:11 2022

@author: chaojunma
"""


colors = ['red','orange','yellow','green','blue','purple']

print(colors)

# Using indexing, print the penultimate color.

print(colors[-2])

# Using indexing, print the 3rd and 4th characters of the penultimate color.

print(colors[-2][2])
print(colors[-2][3])

# Using indexing, remove the color "purple" and add "indigo" and "violet" to the list instead.

colors.pop(colors.index('purple'))

print(colors)

colors.extend(['indigo','violet'])

print(colors)