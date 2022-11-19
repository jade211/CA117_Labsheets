#!/usr/bin/env python3

import sys

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def present(letters, line):
   total = 0
   not_in_line = []
   for letter in letters:
      if letter in line.lower():
         total = total + 1
         if total == 26:
            return ("pangram")
      else:
         if letter not in line.lower():
            not_in_line.append(letter)
   return (f'missing {"".join(not_in_line)}')


for line in sys.stdin:
   line = line.strip()
   result = present(letters, line)
   print(result)
