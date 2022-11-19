#!/usr/bin/env python3

import sys

#def first_word
vertical = []
lines = []
i = 0
for line in sys.stdin.readlines():
   lines.append(line.strip())
#print(lines)
i = 0
while i < len(lines[0]):
   word = ""
   for char in lines:
      #word = ""
      word = word + char[i]
   vertical.append(word)
   i = i + 1
print(vertical)
