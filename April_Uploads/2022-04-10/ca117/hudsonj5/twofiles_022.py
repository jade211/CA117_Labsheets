#!/usr/bin/env python3

import sys
file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, 'r') as f:
    nums1 = f.readlines()
with open(file2, 'r') as g:
    nums2 = g.readlines()

i = 0
while i < len(nums1) and i < len(nums2):
    print(nums1[i].strip())
    print(nums2[i].strip())
    i = i + 1
