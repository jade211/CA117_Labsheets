#!/usr/bin/env python3

dict_book = {")": "(", "}": "{", "]": "["}

class Stack(object):
    def __init__(self):
        self.list = []

    def push(self, input_value):
        self.list.append(input_value)

    def pop(self):
        return self.list.pop() if len(self.list) > 0 else False

    def top(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)

def matcher(line):
    input_line = Stack()
    for bracket in line:
        if bracket in dict_book.values():
            input_line.push(bracket)
        if bracket in dict_book.keys():
            if dict_book[bracket] != input_line.pop():
                return False
    return input_line.is_empty()
