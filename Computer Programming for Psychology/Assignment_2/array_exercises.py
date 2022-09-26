#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: chaojunma
"""

import numpy as np

mixnums = np.array([1,2,3,1.1,2.2,3.3])

print(mixnums)

mixtypes = np.array([1,2,
                      1.1,2.2,
                      '1','2'])

print(mixtypes)


oddarray = np.arange(1,100,2)

print(oddarray)


logarray = np.logspace(1,5,16)

print(logarray)