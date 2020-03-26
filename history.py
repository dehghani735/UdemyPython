List3 = List1 + List2
print(List3)
del List3[0:2]
print(List3)
List1 = ['Item1', 'Item2', 'Item3']
List2 = ['Item4', 'Item5', 'Item6']
List3 = List1 + List2
print(List3)
del List3[0:2]
print(List3)
List3 = List1 + List2
print(List3)
del List3[1:4]
print(List3)
basket = {'Apples', 'Grapes', 'Orange'}
print(type(basket))
set1 = set('fruit1', 'fruit2', 'fruit3')
set1 = set(('fruit1', 'fruit2', 'fruit3'))
tmp = ('fruit1', 'fruit2', 'fruit3')
print(type(tmp))
tmp = ('fruit1', 'fruit2', 'fruit3')
print(type(tmp))
print(type(basket))
set1 = set(('fruit1', 'fruit2', 'fruit3'))  #constructor
print(type(set1))
basket.add('apricot')
print(basket)
print(len(basket))
print(basket)
print(len(basket))
6
basket
basket = {'Apples', 'Grapes', 'Orange'}
print(type(basket))
set1 = set(('fruit1', 'fruit2', 'fruit3'))  #constructor
print(type(set1))
# add an item to existing set
basket.add('apricot')
print(basket)
# check number of items in set
print(len(basket))
basket.remove('Grepes')
basket.remove('Grapes')
print(basket)
S1 = {'apple', 'Oranges', 'Grapes'}
S2 = {'lime', 'grapefruit', 'banana'}
print('Union: ',  S1 | S2)
print('Intersection: ',  S1 & S2)
S1 = {'apple', 'Oranges', 'Grapes', 'banana'}
print('Intersection: ',  S1 & S2)
print('Difference: ',  S1 - S2)
print('Unique elements: ', S1 ^ S2)
tup1 = (1,3,5,7)
tup1[0]
tup1[1]
tup1[2]
tup1[3]
tup3.count(1)
tup3 = (1,1,1,1)
tup3.count(1)
tup4 = (tup2, tup3)
tup2 = (1,'Max', 3+4j)
tup3 = (1,1,1,1)
tup3.count(1)
tup4 = (tup2, tup3)
tup4
c = 12 // 5
print(c)
a = 3 ** 4
print(a)
3 == 3
3 == 4
3 != 3
3 != 4
3<4 and 2>3
3<4 or 2>3
True + True
True + False
False + False
not 3<5
num = int (input('Enter a number:'))
if num < 0:
print(num, ' is negative.')
num = int (input('Enter a number:'))
if num < 0:
print(num, 'is negative.')
else:
print(num, 'is positive.')
runfile('C:/Users/m.dehghani/.spyder-py3/Part2-13FlowControl.py', wdir='C:/Users/m.dehghani/.spyder-py3')

## ---(Sun Mar 22 22:05:09 2020)---
age = 15
status = 'teenager' if age < 12 and age < 20 else 'not teenager'
print(status)
status = 'teenager' if age > 12 and age < 20 else 'not teenager'
print(status)
runfile('C:/Users/m.dehghani/Part2-14Iteration.py', wdir='C:/Users/m.dehghani')
runfile('C:/Users/m.dehghani/Part2-16Functions.py', wdir='C:/Users/m.dehghani')
runfile('C:/Users/m.dehghani/Part2-17VariableScoping.py', wdir='C:/Users/m.dehghani')
%clear
runfile('C:/Users/m.dehghani/Part2-17VariableScoping.py', wdir='C:/Users/m.dehghani')