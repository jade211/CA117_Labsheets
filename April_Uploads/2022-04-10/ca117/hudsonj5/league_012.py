#!/usr/bin/env python3

import sys
def measure(lines):
    largest = 0
    for line in lines:
        line = line.strip()
        if len(line) > largest:
            largest = len(line)
    return largest


clublist = []
lines = sys.stdin.readlines()
for line in lines:
    pieces = line.strip().split()
    clubs = " ".join(pieces[1:-8])
    clublist.append(clubs)
club_length = measure(clublist)

pos, club, p, w, d, l, gf, ga, gd, pts = "POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"
print(f"{pos: >3s} {club: <{club_length}} {p: >2s} {w: >3s} {d: >3s} {l: >3s} {gf: >3s} {ga: >3s} {gd: >3s} {pts: >3s}")

i = 0
while i < len(lines) and i < len(clublist):
   sentence = lines[i]
   input = sentence.split()
   print(f"{input[0]: >3s} {clublist[i]:{club_length}} {input[-8]: >2s} {input[-7]: >3s} {input[-6]: >3s} {input[-5]: >3s} {input[-4]: >3s} {input[-3]: >3s} {input[-2]: >3s} {input[-1]: >3s}")
   i = i + 1
