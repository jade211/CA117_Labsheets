#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
dict = {}

def ordered(s):
   data = s.strip()
   data = data.replace(" ", "")
   data = sorted(data)
   return data


ordered1 = ordered(lines[0])
ordered2 = ordered(lines[1])
dict[ordered1[0]] = ordered2[0]
dict[ordered1[1]] = ordered2[1]
dict[ordered1[2]] = ordered2[2]
#print(ordered1, ordered2)
#print(dict)
print(dict[ordered1[0]] + " " + dict[ordered1[1]] + " " + dict[ordered1[2]])
