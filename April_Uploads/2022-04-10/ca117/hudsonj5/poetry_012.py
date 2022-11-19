#!/usr/bin/env python3

import sys

def measure(lines):
    largest = 0
    for line in lines:
        line = line.strip()
        if len(line) > largest:
            largest = len(line)
    return largest


lines = sys.stdin.readlines()
length = measure(lines)

for line in lines:
    line = line.strip()
    print(f"{line:^{length}}")
