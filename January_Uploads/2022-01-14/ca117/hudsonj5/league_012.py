#!/usr/bin/env python3

import sys
# POS CLUB         P   W   D   L  GF  GA  GD PTS
s = sys.stdin.readlines()
big_line = ""

i = 0
while i < len(s):
   if len(s[i].strip()) > len(big_line):
      big_line = s[i].strip()
   else:
      big_line = big_line
   i = i + 1
club_length = len(big_line.strip())

j = 0
while j < len(s):
   line = s[j]
   line_split = line.split()
   club = (line_split[0] + " " + line_split[1]).strip()
   p = (line_split[2] + " " + line_split[3]).strip()
   print(f"{club}{p: ^{club_length}}")
   j = j + 1
