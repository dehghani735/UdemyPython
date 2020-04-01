# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:16:35 2020

@author: m.dehghani
udemy learn to code from scratch with python 3
"""

cities = {
    'wales' : 'Cardiff',
    'england' : 'London',
    'Scottland': 'Edinburgh'
    }

cities['wales']

dict1 = {}

#===========
#add entry to existing dictionary
cities['France'] = 'Paris'

#===========
# change the value of existing one
cities['wales'] = "Cardiff1"


#===========
#remove an entry
cities.pop('walse')
