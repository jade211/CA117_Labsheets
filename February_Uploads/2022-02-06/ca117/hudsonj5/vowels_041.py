#!/usr/bin/env python3

import sys
import string

paragraph = sys.stdin.read().strip()
vowels = ["a", "e", "i", "o", "u"]
new_paragraph = ""
dict = {}

def decreasing_order(value):
   return value[1]

def dictionary(vowels, new_paragraph, dict):
   for vowel in vowels:
      frequency = new_paragraph.count(vowel)
      dict[vowel] = frequency
   return dict

def remove_punct(new_paragraph, paragraph):
   words = paragraph.strip().split()
   i = 0
   while i < len(words):
      j = 0
      while j < len(words[i]):
         if words[i][0] in string.punctuation:
            words[i] = words[i].replace(words[i][0], "")
         elif words[i][len(words[i]) - 1] in string.punctuation:
            words[i] = words[i].replace(words[i][len(words[i]) - 1], "")
         j = j + 1
      if len(words[i]) == 0:
         words.remove(words[i])
      new_paragraph = new_paragraph + " " + words[i].lower()
      i = i + 1
   return new_paragraph


new_paragraph = remove_punct(new_paragraph, paragraph)
d = dictionary(vowels, new_paragraph, dict)

max_key_width = len(str(max(d.values())))
max_value_width = len(str(max(d.values())))

for key, value in sorted(d.items(), key=decreasing_order, reverse=True):  # could have used key=len instead
   print(f"{key} : {value:>{max_value_width}d}")
