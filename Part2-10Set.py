# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:13:43 2020

@author: m.dehghani
udemy learn to code from scratch with python 3
"""

#create set
basket = {'Apples', 'Grapes', 'Orange'}

print(type(basket))

set1 = set(('fruit1', 'fruit2', 'fruit3'))  #constructor

print(type(set1))

# add an item to existing set
basket.add('apricot')

print(basket)

# check number of items in set
print(len(basket))

# Remove from set

basket.remove('Grapes')

#Remove all items from set
basket.clear()

#=======================
#Set Operation

# Union
S1 = {'apple', 'Oranges', 'Grapes', 'banana'}
S2 = {'lime', 'grapefruit', 'banana'}

print('Union: ',  S1 | S2)

# Intersection
print('Intersection: ',  S1 & S2)

#Difference
print('Difference: ',  S1 - S2)

#unique elements
print('Unique elements: ', S1 ^ S2)
