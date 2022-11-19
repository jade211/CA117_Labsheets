#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
nice = "nice"
d = {}

def find_nice(words):
   for word in words:
      word = word.strip()
      amount = []
      for char in word:
         if char in "nice":
            count = word.count(char)
            amount.append(count)
      d[word] = amount
      if len(amount) > 4:
         d.pop(word)
   return d


result = find_nice(words)
for key, value in result.items():
   print(f"{key}")
