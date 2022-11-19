#!/usr/bin/env python3

import sys

def first_words(lines):
   column = []
   if lines:
      i = 0
      while i < len(lines[0]):
         word = ""
         for char in lines:
            word = word + char[i]
         column.append(word)
         i = i + 1
      return column
   return None


lines = []
for line in sys.stdin.readlines():
   lines.append(line.strip())

word_list = first_words(lines)
if word_list:
   word_list_sorted = sorted(word_list, key=str.lower)
   result = first_words(word_list_sorted)
   if result:
      print("\n".join(result))
