# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:23:55 2020

@author: m.dehghani
udemy learn to code from scratch with python 3
"""

'''
1. Go to IMDB Website to get Top movies
2. we are getting information in tabular format.
3. The data is in the table format. So we need tool to grab information from table 
4. We need to grab data from tables. 
'''

from bs4 import BeautifulSoup
import requests
import re

#import IMDB's top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)