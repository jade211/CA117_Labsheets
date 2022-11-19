#!/usr/bin/env python3

import sys
def multiples3(n):
    result = []
    normal = [int(n) for n in range(1, n + 1)]
    multiples_of_three = [int(n) for n in range(1, n + 1) if n % 3 == 0]
    for num in normal:
        if num in multiples_of_three:
            result.append("X")
        else:
            result.append(num)
    return result


for n in sys.stdin:
    n = int(n)
    print(f"Multiples of 3 replaced: {multiples3(n)}")
