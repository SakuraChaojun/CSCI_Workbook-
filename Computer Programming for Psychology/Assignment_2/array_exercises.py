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


oddarray = np.array(range(0,100+1))

print(oddarray)


logarray = np.array(np.random.lognormal(0,5,16))

print(logarray)