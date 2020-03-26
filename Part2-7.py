# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:32:28 2020

@author: m.dehghani
"""

str1 = "hello"
str2 = "world"
str3 = str1 + str2

print(str3)

# Check Length of String
print (len(str3))

# Check lenght of String

"""
mdt wrote comment 
here :)
"""
print(type(str3))

print(str3[0])

# Access A particular character of a string
str3[0]


# Print Repeating String
print("*" * 50)


# Splitting String
str1 = "This is , Good"

str2 = str1.split(',')

str2[0]
str2[1]

#count
str1.count(' ')

#Replace
str1 = "Hello World"

str1.replace("Hello", "Hi")

#Find
str1.find("Hello")

#=========================================

#complex type

a = 3 + 4j
b = 5 + 6j

c = a + b

print(c.real)
print(c.imag)

#==========================================

#boolean type

c = True

status = bool(input("Ok to proceed:"))

print(type(status))
