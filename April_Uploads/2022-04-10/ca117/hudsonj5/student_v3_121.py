#!/usr/bin/env python3

import sys

subject_points = {"H1": 100, "H2": 88, "H3": 77, "H4": 66, "H5": 56,
                  "O1": 56, "H6": 46, "O2": 46, "O3": 37, "H7": 37,
                  "O4": 28, "O5": 20, "O6": 12, "O7": 0, "O8": 0, "H8": 0}


class Student(object):

    def __init__(self, name, cao):
        self. name = name
        self.cao = cao
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_grade(self, subject):
        if subject in self.grades:
            return self.grades[subject]
        else:
            return "N/A"

    def points(self):
        points = []
        for grade in self.grades.values():
            if grade in subject_points:
                points.append(subject_points[grade])
        points = sorted(points, reverse=True)
        if len(points) >= 3:
            return sum(points[:3])
        else:
            return sum(points)

    def __str__(self):
        info = []
        info.append(f"Name: {self.name:s}")
        info.append(f"CAO: {self.cao:d}")
        info.append(f"Points: {self.points():d}")
        return "\n".join(info)
