# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:23:55 2020

@author: m.dehghani
udemy learn to code from scratch with python 3
"""

def runcalc(x, y):
    return x / y

runcalc(8, 2)

try:
    runcalc(6, 0) #runcalc(6, 2)
except ZeroDivisionError:
    print('Not divide by zero allowed')
except IndexError:
    print('fff')
except FileNotFoundError:
    print('file not found')
except Exception:
    print('General Exception')
else:
    print('All code gets executed without any error')
finally:
    print('I will run everytime')