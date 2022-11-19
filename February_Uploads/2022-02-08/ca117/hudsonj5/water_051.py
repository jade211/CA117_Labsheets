#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()
litres = int(input[0].strip())
buckets = input[1].strip().split()
list = []

for bucket in buckets:
   list.append(int(bucket))

total = 0
i = 0
while i < len(buckets) and litres >= list[i]:
   if litres - list[i] >= 0:
      total = total + 1
      litres = litres - list[i]
      total = total
   i = i + 1

print(total)
