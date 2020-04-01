# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 17:26:55 2020

@author: m.dehghani
"""


class Person:

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def __init__(self, name, age):
        super().__init__()
        #Person.instance_count += 1
        Person.increment_instance_count()
        self.name = name
        self.age = age
    
    def birthday(self):
        print('Happy Birthday, You were', self.age)
        self.age += 1
        print('You are now', self.age)

    @staticmethod
    def static_function():
        print('I am static method')

Person.static_function()