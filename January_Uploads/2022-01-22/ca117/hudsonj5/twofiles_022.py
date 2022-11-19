#!/usr/bin/env python3

import sys
input = sys.argv[1:]

def readfile(file1, file2):
   with open(file1, "r") as f:
      number1 = f.readlines()
   with open(file2, "r") as g:
      number2 = g.readlines()
   return number1, number2


list1, list2 = readfile(input[0], input[1])
i = 0
while i < len(list1) and i < len(list2):
   print(list1[i].strip())
   print(list2[i].strip())
   i = i + 1
