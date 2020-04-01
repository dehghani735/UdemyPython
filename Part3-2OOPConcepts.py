# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:26:55 2020

@author: m.dehghani
"""

class Car:
    def __init__(self, year, make):
        super().__init__()
        self.__year = year
        self.__make = make

beetel = Car(2019, "Beetel")
mini = Car(2019, "Mini")
polo = Car(2019, "Polo")

print(type(polo))