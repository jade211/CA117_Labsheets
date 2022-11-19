#!/usr/bin/env python3

subjects = {"english": 0, "irish": 0, "french": 0, "spanish": 0}

def max_value(d):
    values = list(d.values())
    keys = list(d.keys())
    return keys[values.index(max(values))]


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
        for k, v in self.grades.items():
            if k in subjects:
                for k, v in subjects.items():
                    subjects[k] = v + 1
            return (max_value(subjects))

    def __str__(self):
        info = []
        for v in sorted(self.classbook.values(), key=increasing):
            info.append(f"{v}")
        return "\n".join(info)
