# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:26:55 2020

@author: m.dehghani
"""

def multiply(a, b):
    return a * b

def multiby( func, num):
    return lambda y : func(y, num)

# double is a function; a curried function
double = multiby(multiply, 2)

print( double(2))

# triple is a function; a curried function
triple = multiby(multiply, 3)

print(triple(5))
