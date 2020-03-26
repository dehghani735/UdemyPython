# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:26:55 2020

@author: m.dehghani
"""

# ==
3 == 3

3 == 4

# !=
3 != 3
3 != 4

# and

3<4 and 2>3

# or
3<4 or 2>3

#
True + True
True + False
False + False

# not
not 3<5

# If exmple

num = int (input('Enter a number:'))

if num < 0:
    print(num, 'is negative.')
elif num > 0:
    print(num, 'is positive.')
else:
    print(num, 'is zero.')
    
#Nested if
snowing = True
temp = -1
if temp < 0:
    print('It is freezing.')
    if snowing:
        print('It is snowing.')
    print('Eat hot choclate')
print('bye')


#==============
#If Expression

age = 15
status = 'teenager' if age > 12 and age < 20 else 'not teenager'
print(status)
