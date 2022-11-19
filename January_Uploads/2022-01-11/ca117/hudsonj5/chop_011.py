#!/usr/bin/env/python3

import sys

def chop(s):  # creates a function that strips first and last
   return s[1:len(s) - 1]


for sentence in sys.stdin:  # reads input
   s = sentence.strip()  # removes /n
   chopped = chop(s)
   if len(chopped) > 0:
      print(chopped)
