# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:34:30 2020

@author: m.dehghani
"""

def Addition(input1, input2 = 5):
    return input1 + input2

def Substraction(input1, input2):
    return input1 - input2

def Division(input1, input2):
    return input1 / input2

def Multiplication(input1, input2):
    return input1 * input2

def MultiAddition(*args):
    total = 0
    for i in args:
        total += i
    return total

Add = Addition(input2 = 2, input1 = 3)
print(Add)

Substract = Substraction(3,2)
print(Substract)

Multi = Multiplication(6, 5)
print(Multi)

Divide = Division(4,2)
print(Divide)

addnvalue = MultiAddition(2,3,4,5,6,7,8)
print(addnvalue)

#========================

def named(**kwargs):
    for key in kwargs.keys():
        print('arg:', key, 'has value:', kwargs[key])

named(a=1, b=2, c=3)

named(a=1, b=2, c=3, d=4, e=5)

#========================
#Anonymous Function
# lambda arguments : expression
double = lambda i : i * 2

print(double(3))