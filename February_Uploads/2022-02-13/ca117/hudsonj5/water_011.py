#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()
total = 0
litres = input[0].strip()
bucket_capacity = input[1].strip().split()

i = 0
while i < len(bucket_capacity) and int(litres) >= int(bucket_capacity[i]):
   if int(litres) - int(bucket_capacity[i]) >= 0:
      total = total + 1
      litres = int(litres) - int(bucket_capacity[i])
   else:
      total = total
   i = i + 1
print(total)
