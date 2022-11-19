#!/usr/bin/env python3

import sys
names = []
marks = []
best_marks = 0
best_student = ""

file = sys.argv[1]
try:
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            marks.append(int(line[0]))
            names.append(" ".join(line[1:]))
        i = 0
        while i < len(marks) and i < len(names):
            if marks[i] > best_marks:
                best_marks = marks[i]
                best_student = names[i]
            i = i + 1
        print(f"Best student: {best_student}")
        print(f"Best mark: {best_marks}")

except FileNotFoundError:
    print(f"The file {file} could not be opened.")
