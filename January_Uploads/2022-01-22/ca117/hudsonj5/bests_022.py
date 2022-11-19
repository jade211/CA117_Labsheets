#!/usr/bin/env python3

import sys

file = sys.argv[1]
scores = []
names = []
name_of_best_students = []
try:
   with open(file, 'r') as f:
      line = f.readlines()
      i = 0
      while i < len(line):
         biggest = 0
         split = (line[i].strip().split())
         try:

            scores.append(int(split[0]))
            names.append(split[1:])

         except ValueError:
            print("Invalid mark " + split[0] + " encountered. Skipping.")
         i = i + 1
      j = 0
      while j < len(scores) and j < len(names):
         if int(scores[j]) > biggest:
            biggest = scores[j]
            names_of_best = " ".join(names[j])
         elif int(scores[j]) == biggest:
            names_of_best = names_of_best + ", " + " ".join(names[j])
         j = j + 1

except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")

print(f"Best student(s): {names_of_best}")
print(f"Best mark: {biggest}")
