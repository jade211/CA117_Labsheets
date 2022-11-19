#!/usr/bin/env python3

import sys

# For any three cakes bought the cheapest of the three comes free.
# For each line the program should output the minimum amount
# required to purchase those cakes
# (i.e. assume each customer groups their cakes in order
# to optimise their savings).

def free_cake(new_line):
    total = 0
    groups_of_three = [new_line[i:i + 3] for i in range(0, len(new_line), 3)]
    for group in groups_of_three:
        if len(group) >= 3:
            for cake in group:
                total = total + cake
            total = total - min(group)
        else:
            for cake in group:
                total = total + cake
    return total


for line in sys.stdin.readlines():
    line = line.strip().split()
    new_line = []
    for str_cakes in line:
        int_cakes = int(str_cakes)
        new_line.append(int_cakes)
    result = free_cake(sorted(new_line, reverse=True))
    print(result)
