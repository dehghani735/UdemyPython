# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:26:55 2020

@author: m.dehghani
"""

class Person:
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
    
    def birthday(self):
        print('Happy Birthday, You were', self.age)
        self.age += 1
        print('You are now', self.age)

p1 = Person("MDT", 26)
p2 = Person("MST", 25)
p3 = Person("MRDT", 24)

print(p1)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)

p1.birthday()

del p1

print(p2.__class__)

print(filter.__doc__)
print(filter.__dict__)
print(filter.__module__)