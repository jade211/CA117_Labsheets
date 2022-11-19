#!/usr/bin/env python3

cao_points = {"H1": 100, "H2": 88, "H3": 77, "H4": 66, "H5": 56, "O1": 56, "H6": 46, "O2": 46, "H7": 37, "O3": 37, "O4": 28, "O5": 20, "O6": 12, "H8": 0, "O7": 0, "O8": 0}

def tagger(items):
    return items[1]

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

    # def points(self):
    #     cao_list = []
    #     for k, v in sorted(self.grades.items(), key=tagger):
    #         cao_list.append(cao_points[v])
    #     if cao_list is None:
    #         return 0
    #     else:
    #         while len(cao_list) > 3:
    #             cao_list.remove(min(cao_list))
    #         return sum(cao_list)

    def points(self):
        gotten_points = []
        cao_gotten_list = []
        final = []
        total = 0
        for v in self.grades.values():
            cao_gotten_list.append(f"{v}")  # h8, h6
        for grade in cao_gotten_list:
            if grade in cao_points:
                gotten_points.append(cao_points[grade])
        gotten_points = sorted(gotten_points, reverse=True)
        if len(gotten_points) > 3:
            final = gotten_points[:3]
            for point in final:
                total = total + int(point)
        else:
            final = gotten_points
            for point in final:
                total = total + int(point)
        return total

    def __str__(self):
        info = []
        info.append(f"Name: {self.name}")
        info.append(f"CAO: {self.cao}")
        info.append(f"Points: {self.points()}")
        return "\n".join(info)

    def __eq__(self, other):
        return self.points() == other.points()

    def __gt__(self, other):
        return self.points() > other.points()

    def __lt__(self, other):
        return self.points() < other.points()
