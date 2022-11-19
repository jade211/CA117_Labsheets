#!/usr/bin/env python3

import sys

def capitalise(s):
   return s[0].upper() + s[1: len(s) - 1] + s[len(s) - 1].upper()


for sentence in sys.stdin:
   s = sentence.strip()
   capital = capitalise(s)
   if len(s) >= 2:
      print(capital)
