#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
big_line = ""
i = 0
while i < len(s):
   if len(s[i].strip()) > len(big_line):
      big_line = s[i].strip()
   else:
      big_line = big_line
   i = i + 1

n = len(big_line.strip())

j = 0
while j < len(s):
   s[j] = s[j].strip()
   print(f"{s[j]: ^{n}}")
   j = j + 1
