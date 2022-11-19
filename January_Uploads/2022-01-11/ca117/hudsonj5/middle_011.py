#!/usr/bin/env/python3

import sys

def middle(s):
   return s[len(s) // 2]


for sentence in sys.stdin:
   s = sentence.strip()
   middle_character = middle(s)
   if len(s) % 2 == 1:
      print(middle_character)
   else:
      print("No middle character!")
