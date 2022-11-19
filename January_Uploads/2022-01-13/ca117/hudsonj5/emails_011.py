#!/usr/bin/env python3

import sys

def names(s):
   split = s.strip().split(".")
   return split[0: 2]


for name in sys.stdin:
   s = name
   name = names(s)
   i = 0
   while i < len(name[1]) and not (name[1][i] >= "0" and name[1][i] <= "9"):
      i = i + 1

   if i < len(name[1]):
      second_name = (name[1][0: i])
      first_name = name[0]
      first_name = first_name.capitalize()
      second_name = second_name.capitalize()
      print(first_name + " " + second_name)
