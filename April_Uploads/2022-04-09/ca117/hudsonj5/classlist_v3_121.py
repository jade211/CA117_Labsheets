#!/usr/bin/env python3

subjects = {}

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


def increasing(v):
    return v.cao

def max_values(d):
    values = list(d.values())
    keys = list(d.keys())
    return keys[values.index(max(values))]


subjects = []
subject_counter = {}

class Classlist(object):

    def __init__(self):
        self.classbook = {}

    def add(self, student):
        self.classbook[student.cao] = student
        self.grades = student.grades

    def remove(self, number):
        if number in self.classbook:
            del self.classbook[number]

    def lookup(self, number):
        if number in self.classbook:
            return self.classbook[number]

    def most_popular_subject(self):
        for v in self.classbook:
            for key in self.grades.keys():
                subjects.append(key)
            for subject in subjects:
                subject_counter[subject] = subjects.count(subject)
        return max_values(subject_counter)

    def __str__(self):
        info = []
        for v in sorted(self.classbook.values(), key=increasing):
            info.append(f"{v}")
        return "\n".join(info)
