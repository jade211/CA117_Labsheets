#!/usr/bin/env python3

import sys

water = sys.stdin.readlines()
litres, bucket = int(water[0].strip()), water[1].strip().split()
total = 0
i = 0
while i < len(bucket) and int(bucket[i]) <= litres:
    ind_bucket = int(bucket[i].strip())
    if litres >= 0:
        litres = litres - ind_bucket
        total = total + 1
    i = i + 1
print(total)
