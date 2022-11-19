#!/usr/bin/env python3

import sys
import string

new_words = []

def remove_punct(s):
   s = s.lower()
   s = s.strip()
   words = s.split()
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
      i = i + 1
   return words


for lines in sys.stdin:
   no_punct = remove_punct(lines)
   words = no_punct
   i = 0
   while i < len(words):
      if words[i] not in new_words:
         new_words.append(words[i])
      i = i + 1
print(len(new_words))
