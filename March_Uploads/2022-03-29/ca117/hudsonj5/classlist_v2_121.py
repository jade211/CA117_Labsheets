#!/usr/bin/env python3

def increasing(v):
    return v.cao

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        info = []
        info.append(f"Name: {self.name}")
        info.append(f"CAO: {self.cao}")
        return "\n".join(info)

class Classlist(object):

    def __init__(self):
        self.classbook = {}

    def add(self, student):
        self.classbook[student.cao] = student

    def remove(self, number):
        if number in self.classbook:
            del self.classbook[number]

    def lookup(self, number):
        if number in self.classbook:
            return self.classbook[number]

    def __str__(self):
        info = []
        for v in sorted(self.classbook.values(), key=increasing):
            info.append(f"{v}")
        return "\n".join(info)
