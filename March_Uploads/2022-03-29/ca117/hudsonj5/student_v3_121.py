#!/usr/bin/env python3

# A student’s CAO points are calculated by
# summing the points awarded for their three top-scoring subjects.

# Where a student has three or fewer
# recorded grades their CAO points is the sum of all their points.

cao_points = {"H1": 100, "H2": 88, "H3": 77, "H4": 66, "H5": 56, "H6": 46, "H7": 37, "H8": 0,
              "O1": 56, "O2": 46, "O3": 37, "O4": 28, "O5": 20, "O6": 12, "O7": 0, "O8": 0}

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

    def points(self):
        cao_list = []
        total = 0
        for v in sorted(self.grades.values()):
            cao_list.append(f"{v}")
        for value in cao_list:
            if len(cao_list) > 3:
                if value in cao_list[0:3]:
                    total = total + cao_points[value]
            else:
                total = total + cao_points[value]
        return total

    def __str__(self):
        info = []
        info.append(f"Name: {self.name}")
        info.append(f"CAO: {self.cao}")
        info.append(f"Points: {self.points()}")
        return "\n".join(info)
