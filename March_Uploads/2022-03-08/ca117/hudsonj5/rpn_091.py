#!/usr/bin/env python3

from math import sqrt

binops = {'+': float.__add__,
          '-': float.__sub__,
          '*': float.__mul__,
          '/': float.__truediv__}

uniops = {'n': float.__neg__,
          'r': sqrt}

class Stack(object):
    def __init__(self):
        self.list = []

    def push(self, input_value):
        self.list.append(input_value)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)


def __add__(x, y):
    return x + y

def __sub__(x, y):
    return x - y

def __mul__(x, y):
    return x * y

def __truediv__(x, y):
    return x / y

def __neg__(x):
    return -x


def calculator(line):
    input_line = Stack()

    for character in line.split():
        if character in binops.keys():
            y = input_line.pop()
            x = input_line.pop()
            input_line.push(binops[character](x, y))
        elif character in uniops.keys():
            input_line.push(uniops[character](input_line.pop()))
        else:
            input_line.push(float(character))
    return input_line.top()
