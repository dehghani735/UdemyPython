# -*- coding: utf-8 -*-
"""
Created on Wed Apr 02 22:15:43 2020

@author: m.dehghani
Orielly Python DS
"""


aList = [1,4,3,2]

aList.append(-5)
aList.sort()

aList[0] = 99

for _ in aList:
    print(_)

#-------------
aTuple = (3, 5, 'string')

print(aTuple)

len(aTuple)

aTuple[0] = 'ali'

for _ in aTuple:
    print(_)

#------------
#dictionary
a = {11: 99, 2:137}

print(len(a))  # number of pairs

print(a[2]) # what is associate with 2
print(a[11]) # what is associate with 11

print(a[5]) # this gives an error -> invalid key

a[2] = 6

a

#------------
s = {2, 4, 6}
print(len(s))
s.add(6)
print(len(s))

#------
#deque
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.popleft()
d.append(4)
d.append(5)
d.pop()

d.popleft()
d