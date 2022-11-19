#!/usr/bin/env python3

import sys

def quadrant(x, y):
    if x >= 1 and y >= 1:
        return 1
    elif x >= 1 and y <= -1:
        return 2
    elif x <= -1 and y <= -1:
        return 3
    else:
        return 4


lines = sys.stdin.readlines()
for point in lines:
    point = point.strip().split()
    x, y = int(point[0]), int(point[1])
    print(quadrant(x, y))
