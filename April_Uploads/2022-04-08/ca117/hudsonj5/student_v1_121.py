#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        info = []
        info.append(f"Name: {self.name}")
        info.append(f"CAO: {self.cao}")
        return "\n".join(info)
