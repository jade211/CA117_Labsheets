#!/usr/bin/env python3

import string

# Your program should output a comma-separated 
# list of all words read from stdin that match the supplied pattern.


import sys

def punct(word):
    for char in words:
        if char in string.punctuation:
            word = word.replace(char, "")
    return word

lines = sys.stdin.readlines()
words = lines[0]
pattern = lines[1:]

result = punct(pattern)