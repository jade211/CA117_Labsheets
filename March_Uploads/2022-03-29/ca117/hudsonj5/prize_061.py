#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

integer = int(lines[0].strip())  # starting position
swaps = lines[1].strip()  # swaps to be done

for letter in swaps:
   if integer == 1 and letter == "A":
      integer = integer + 1
   elif integer == 2 and letter == "A":
      integer = integer - 1
   elif integer == 2 and letter == "B":
      integer = integer + 1
   elif integer == 3 and letter == "B":
      integer = integer - 1
   elif integer == 1 and letter == "C":
      integer = integer + 2
   elif integer == 3 and letter == "C":
      integer = integer - 2
print(integer)
