#!/usr/bin/env python3

import sys

def first_words(lines):
   column = []
   i = 0
   while i < len(lines[0]):
      word = ""
      for char in lines:
         word = word + char[i]
      column.append(word)
      i = i + 1
   return column


lines = []
for line in sys.stdin.readlines():
   lines.append(line.strip())

word_list = first_words(lines)
word_list_sorted = sorted(word_list, key=str.lower)

print("\n".join(first_words(word_list_sorted)))
