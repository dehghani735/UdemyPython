# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:42:28 2020

@author: m.dehghani
udemy learn to code from scratch with python 3
"""

count = 0
print('Starting')

while count<10:
    print(count, ' ', end = '')
    count+=1
print()
print('Done')

#For

for i in range(0, 10):
    print(i, ' ', end = '')
print()
print('Done')


for i in range(0, 10, 2):
    print(i, ' ', end = '')
print()
print('Done')

#========
#break
'''
num = int(input('Enter a number to continue:'))
for i in range(0, 10, 2):
    if i == num:
        break
    print(i, ' ', end = '')
print()
print('Done')
'''
#========
# continue

for i in range(0, 10):
    print(i, ' ', end = '')
    if i % 2 == 1:
        continue
    print('hey it is an even number')
print('Done')

#========
# For loop with else

num = int(input('Enter a number for for else:'))
for i in range(0, 10, 2):
    if i == num:
        break
    print(i, ' ', end = '')
else:
    print()
    print('All condition ran successfully')
print()
print('Done')
