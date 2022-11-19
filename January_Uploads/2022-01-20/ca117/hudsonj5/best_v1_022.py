#!/usr/bin/env python3

import sys

file = sys.argv[1]
scores = []
names = []

try:
   with open(file, 'r') as f:
      line = f.readlines()
      i = 0
      while i < len(line):
         biggest = 0
         split = (line[i].strip().split())
         scores.append(split[0])
         names.append(split[1:])
         i = i + 1
      j = 0
      while j < len(scores) and j < len(names):
         if int(scores[j]) > biggest:
            biggest = int(scores[j])
            name_of_biggest = names[j]
            name_of_biggest = " ".join(name_of_biggest)
         j = j + 1

   f.close()

except FileNotFoundError:
   print(f"The file {sys.argv[1]} could not be opened.")

print(f"Best student: {name_of_biggest}")
print(f"Best mark: {biggest}")
