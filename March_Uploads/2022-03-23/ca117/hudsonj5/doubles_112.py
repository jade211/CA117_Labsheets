#!/usr/bin/env python3

import sys

def max_value(d):
   values = list(d.values())
   keys = list(d.keys())
   return keys[values.index(max(values))]

def double_vowel(doubles):
   d = {}
   for word in doubles:
      total = word.count("aa") + word.count("ee") + word.count("ii") + word.count("oo") + word.count("uu")
      d[word] = total
   return d


word_list = []
for word in sys.stdin:
   word = word.strip()
   word_list.append(word)
   doubles = [w for w in word_list if "aa" in w or "ee" in w or "ii" in w or "oo" in w or "uu" in w]
   result_dict = double_vowel(doubles)

print(max_value(result_dict))
