#!/usr/bin/env python3

import sys
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"


def count(string):
   for char in string:
      if char in lower:
         string = string.replace(char, " ")
   uppers = string.split()
   longest = ""
   for upper in uppers:
      if len(uppers) > len(longest):
         longest = upper
   return longest


for string in sys.stdin:
   string = string.strip()
   total = count(string)
   print(total)
