#!/usr/bin/env python3

import sys
paragraph = sys.stdin.read()

def order(value):
   return value[1]

def vowel(paragraph):
   d = {}
   for char in paragraph.lower():
      total = 0
      if char in "aeiou":
         total = paragraph.lower().count(char)
         d[char] = total
   return d


d_vowel = vowel(paragraph)
max_value_width = len(str(max(d_vowel.values())))
max_key_value = len(str(max(d_vowel.keys())))

for key, value in sorted(d_vowel.items(), key=order, reverse=True):
   print(f"{key} : {value:>{max_value_width}d}")
