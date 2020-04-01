# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:23:55 2020

@author: m.dehghani
"""
#public access
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

emp1 = Employee('MDT', '10000000')
print(emp1.salary)

#protected access
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self._salary = sal

class payroll(Employee):
    def salgen(self):
        print('Salary Generated')

E1 = Employee('David', 4345)
E1._salary

p1 = payroll('David', 4345)
p1._salary

#private access
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.__salary = sal
    
    def giveEmpSalary(self):
        print(self.name, 'Employee salary', self.__salary)

E2 = Employee('David', 7343)
E2.giveEmpSalary()

