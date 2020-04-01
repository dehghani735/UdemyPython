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
    
    def birthday(self):
        print('Happy Birthday, you were,', self.age)
        self.age += 1
        print('You are now', self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
        
    def recalculate_pay(self, hours_worked):
        rate_of_pay = 8.5
        if self.age >= 21:
            rate_of_pay += 2.8
        return rate_of_pay * hours_worked

class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        super().__init__(name, age, id)
        self.region = region
        self.sales = sales

    def bonus(self):
        return self.sales * 0.6
    
# Create objects of Classes

print('Person')
p = Person('Ali', 39)
print(p)
print('=' * 25)

print('Employee')
e = Employee('Monica', 28, 444)
e.birthday()
print('e.calculate_pay(40)', e.recalculate_pay(40))
print('=' * 25)

print('SalesPerson')
s = SalesPerson('Jack', 34, 6712, 'Yazd', 400000)
s.birthday()
print('s.calculate_pay(50)', s.recalculate_pay(50))
print('s.bonus()', s.bonus())

