#!/usr/bin/env/python3

import sys

def capitalise(s):
   return s.upper()


for sentence in sys.stdin:
   s = sentence.strip()
   s = s.split()
   string1 = capitalise(s[0])
   string2 = capitalise(s[1])
   print(string1 in string2)
