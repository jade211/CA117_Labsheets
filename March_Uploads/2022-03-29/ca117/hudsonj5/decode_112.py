#!/usr/bin/env python3

import sys

d = {"apa": "a",
     "epe": "e",
     "ipi": "i",
     "opo": "o",
     "upu": "u"}

# After each vowel he adds a p followed by the vowel again.
# Write a program called decode_112.py that decodes Jimmy’s messages.
# Eg: papa = pa(pa)pa(pa)

def vowel_funct(word):
   for key, value in d.items():
      if key in word:
         word = word.replace(key, value)
   return word


for word in sys.stdin:
   print(vowel_funct(word.strip()))
