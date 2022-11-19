#!/usr/bin/env python3

import sys

d = {}
def smallest(time):
   mins, seconds = time.split(":")
   total = (int(mins) * 60 + int(seconds))
   return total

def number_order(d):
   return smallest((d[- 1]))


for input in sys.stdin:
   input = input.strip().split()
   name = input[0]
   times = input[1:]

   try:
      d[name] = min(times, key=smallest)
   except ValueError:
      continue  # continue will skip over person and not add to d

smallest = (min(d.items(), key=number_order))
name = smallest[0]
time = smallest[1]
print(f"{name} : {time}")
