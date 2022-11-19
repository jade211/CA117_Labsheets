#!/usr/bin/env python3

import sys
def fizz_buzz(x, y, n):
    if i % x == 0 and i % y == 0:
        return f"fizzbuzz"
    if i % x == 0:
        return f"fizz"
    if i % y == 0:
        return f"buzz"
    else:
        return i


nums = sys.stdin.readline().strip().split()
x, y, n = int(nums[0]), int(nums[1]), int(nums[2])
for i in range(1, n + 1):
    print(fizz_buzz(x, y, i))
