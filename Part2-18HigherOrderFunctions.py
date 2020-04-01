# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:26:55 2020

@author: m.dehghani
"""
from functools import reduce

numbers = range(0, 10)
even = []
print(type(numbers))

for i in numbers:
    if i%2 == 0:
        even.append(i)

print('even numbers:', even)
#========================
#Filter
def is_even(x):
    return x%2 == 0

even_hof = list(filter(is_even, numbers))

print(even_hof)

#========================
#Map
number = range(0, 10)

square = list(map(lambda x : x * x, number))

print(square)

#=======================
#Reduce

number = range(1, 10)

reduced_val = reduce(lambda x, y: x * y, number)

print(reduced_val)