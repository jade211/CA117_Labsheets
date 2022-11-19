#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split("@")
    name, email = line[0], line[1]
    for char in name:
        if char in "1234567890":
            name = name.replace(char, "")
    name = name.split(".")
    name_lst = []
    for word in name:
        name_lst.append(word.title())
    print(" ".join(name_lst))
