#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_grade(self, subject):
        if subject in self.grades:
            return self.grades[subject]
        else:
            return f"N/A"

    def __str__(self):
        info = []
        info.append(f"Name: {self.name}")
        info.append(f"CAO: {self.cao}")
        return "\n".join(info)
