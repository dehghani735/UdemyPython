# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:15:43 2020

@author: m.dehghani
"""

#List
#Create List
List1 = ['Item1', 45]

#Accessing List
List1[0]
List1[1]

#Add item to a list
List1.append('Item2')

print(List1)

#Insert at a particular position
List1.insert(1, 'Item3')

print(List1)

#concatenation
List1 = ['Item1', 'Item2', 'Item3']
List2 = ['Item4', 'Item5', 'Item6']

List3 = List1 + List2

print(List3)

# del from 1 til 4 (include 1, exclude 4)
del List3[1:4]
