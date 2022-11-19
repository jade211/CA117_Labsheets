#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()
total = 0
litres = input[0].strip()
bucket_capacity = input[1].strip().split()
integer = []

j = 0
while j < len(bucket_capacity):
   integer.append(int(bucket_capacity[j]))
   j = j + 1

i = 0
while i < len(bucket_capacity) and int(litres) >= integer[i]:
   if int(litres) - integer[i] >= 0:
      total = total + 1
      litres = int(litres) - integer[i]
   else:
      total = total
   i = i + 1
print(total)
