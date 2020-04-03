# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 10:15:43 2020

@author: m.dehghani
Orielly Python DS
"""
from circBuffer import CircularBuffer

# This class extends CircularBuffer


class MovingAverage(CircularBuffer):
    def __init__(self, size):
        CircularBuffer.__init__(self, size)
        self.total = 0

    def getAverage(self):
        if self.count == 0:
            return 0
        return self.total / self.count

    def remove(self):
        removed = CircularBuffer.remove(self)
        self.total -= removed
        return removed

    def add(self, value):
        if self.isFull():
            delta = -self.buffer[self.low]
        else:
            delta = 0
        delta += value
        self.total += delta
        CircularBuffer.add(self, value)

    def __repr__(self):
        if self.isEmpty():
            return 'ma:[]'

        return 'ma: [' + ','.join(map(str, self)) + ']:' + str(self.getAverage())


ma = MovingAverage(4)
ma.add(5)
ma.add(6)
ma.add(3)
ma.add(9)

print(ma)


def fibonacci(n):
    a = b = 1
    result = [a, b]
    while n > 2:
        n = n - 1
        a, b = b, a+b
        result.append(b)
    return result


def fibonacciGen(n):
    a = b = 1
    yield a
    yield b
    while n > 2:
        n -= 1
        a, b = b, a+b
        yield b


for _ in fibonacci(10):
    print(_)

for _ in fibonacciGen(10):
    print(_)
