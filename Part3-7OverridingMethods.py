# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:23:55 2020

@author: m.dehghani
"""

class Person:
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
    
    def __str__(self):
        return 'Person ' + self.name + ' is ' + str(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    
    def __str__(self):
        return 'Employee ' + self.name + ' is ' + str(self.age) + ' and id is: ' + str(self.id)
    
# Create objects of Classes
p = Person('mdt', 26)
print(p)

e = Employee('Randy', 27, 7535)
print(e)
