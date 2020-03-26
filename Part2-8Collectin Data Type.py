# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:16:35 2020

@author: m.dehghani
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
