#!/usr/bin/env python3

import sys

def count(s):
   s = s.strip()
   total = 0
   number = any(char.isdigit() for char in s)
   if number is True:
      total = total + 1
   else:
      total = total
   small_letter = any(char.islower() for char in s)
   if small_letter is True:
      total = total + 1
   else:
      total = total
   big_letter = any(char.isupper() for char in s)
   if big_letter is True:
      total = total + 1
   else:
      total = total
   special_chars = any(not char.isalnum() for char in s)
   if special_chars is True:
      total = total + 1
   else:
      total = total
   return total


for sentence in sys.stdin:
   s = sentence
   total = count(s)
   print(total)
