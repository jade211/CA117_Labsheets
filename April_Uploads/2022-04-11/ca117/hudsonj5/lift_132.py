#!/usr/bin/env python3

import sys
info = sys.stdin.readline().strip().split()
floor_total, current, floor, up_amount, down_amount = int(info[0]), int(info[1]), int(info[2]), int(info[3]), int(info[4])

# currectly on s (1)
# pressing up goes + u steps (2)
# pressing down goes - d steps (1)

# has f floors (10)
# trying to get to g (10)

count = 0
floor_moving = 0

i = 0
while i <= floor_total and current != floor:
    if floor > current:
        current = current + up_amount
        count = count + 1
    if floor < current:
        current = current - down_amount
        count = count + 1
    i = i + 1
if i < floor_total:
    print(count)
if i >= floor_total:
    print("Sorry Sheila!")
