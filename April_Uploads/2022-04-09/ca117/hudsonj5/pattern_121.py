#!/usr/bin/env python3

import sys
def punct(match):
    position = []
    i = 0
    while i < len(match):
        if match[i] == "-":
            position.append(i)
        i = i + 1
    return position

def dashes(word, position):
    for i in position:
        word = word[:i] + "-" + word[i + 1:]
    return word


lines = sys.stdin.readlines()
match = lines[0].strip()
pattern = lines[1:]

possible = []
for word in pattern:
    word = word.strip()
    if len(word) == len(match):
        possible.append(word)

position = punct(match)
result = []
for word in possible:
    word_match = dashes(word, position)
    if word_match == match:
        result.append(word)
if result:
    print(", ".join(result))

# import sys
# from re import findall

# lines = sys.stdin.readlines()
# p = lines[0].replace('-', '[a-z]')
# #print(p)
# match = []
# for line in lines[1:]:
#    s = findall(p, line)
#    if s:
#       match.append(s[0].strip())
# if match:
#    print(', '.join(match))
