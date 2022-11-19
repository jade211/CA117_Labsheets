#!/usr/bin/env python3

import sys
input = sys.argv[1]
paragraph = sys.stdin.readlines()

def censor(file1):
   with open(file1, "r") as f:
      words = (f.readlines())
   return words


words = censor(input)
sonnet = paragraph

for words in words:
   word = words.strip()
   j = 0
   while j < len(sonnet):
      if word in sonnet[j]:
         sonnet[j] = sonnet[j].replace(word, "@" * len(word))
      j = j + 1

print("".join(sonnet).strip())
