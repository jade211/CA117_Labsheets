#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()
big_line = ""
club_names = []

i = 0
while i < len(s):
   line = s[i]
   name = line.split()
   club = " ".join(name[1: -8])
   club_names.append(club)
   i = i + 1

j = 0
while j < len(club_names):
   if len(club_names[j]) > len(big_line):
      big_line = club_names[j]
   else:
      big_line = big_line
   j = j + 1
club_length = len(big_line.strip())

pos = "POS"
club = "CLUB"
p = "P"
w = "W"
d = "D"
L = "L"
gf = "GF"
ga = "GA"
gd = "GD"
pts = "PTS"
print(f"{pos: >3s} {club: <{club_length}} {p: >2s} {w: >3s} {d: >3s} {L: >3s} {gf: >3s} {ga: >3s} {gd: >3s} {pts: >3s}")

j = 0
while j < len(s) and j < len(club_names):
   sentence = s[j]
   input = sentence.split()
   print(f"{input[0]: >3s} {club_names[j]:{club_length}} {input[-8]: >2s} {input[-7]: >3s} {input[-6]: >3s} {input[-5]: >3s} {input[-4]: >3s} {input[-3]: >3s} {input[-2]: >3s} {input[-1]: >3s}")
   j = j + 1
