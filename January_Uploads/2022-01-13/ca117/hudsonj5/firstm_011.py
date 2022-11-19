#!/usr/bin/env python3

import sys

def capital(s):
   return s.replace("m", "M", 1)


for sentence in sys.stdin:
   s = sentence.strip()
   new_sentence = capital(s)
   print(new_sentence)
