# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 13:15:43 2020

@author: m.dehghani
Orielly Python DS
"""

# Performance Computation

import random
import timeit

for trial in [2**_ for _ in range(1, 9)]:
    numbers = [random.randint(1, 9) for _ in range(trial)]
    m = timeit.timeit(stmt='sum = 0\nfor d in numbers:\n\tsum = sum + d',
        setup='import random\nnumbers = ' + str(numbers)) 
    print('{0:d} {1:f}'.format(trial, m))

# setup parameter allows some initial code executed first before any timing proceeds
