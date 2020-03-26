# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:44:55 2020

@author: m.dehghani
"""
g = 10


def fun1():
    a = 1
    print(a)


def fun2():
    b = 2
    print(b)
    print(g)


fun2()

# ===============

max = 100


def print_max():
    global max
    max = max + 1
    print(max)


print_max()

print('max is', max)
