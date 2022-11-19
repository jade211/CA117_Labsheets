#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

integer = lines[0].strip()  # starting position
swaps = lines[1].strip().split()  # swaps to be done

for letter in swaps:
   if integer == 1:
      if letter == "A":
         integer = 2
      elif letter == "B":
         integer = 1
      elif letter == "C":
         integer == 3
 
   elif integer == 2:
      if letter == "A":
         integer = 1
      elif letter == "B":
         integer = 3
      elif letter == "C":
         integer == 2

   elif integer == 3:
      if letter == "A":
         integer = 3
      elif letter == "B":
         integer = 2
      elif letter == "C":
         integer == 1
   print(integer)
