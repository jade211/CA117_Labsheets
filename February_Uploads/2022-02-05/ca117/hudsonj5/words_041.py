#!/usr/bin/env python3

import sys
import string
paragraph = sys.stdin.read().strip()
new_paragraph = ""
dict = {}

def alphabetical(item):
   return item[0]


def dictionary(new_paragraph, dict):
   words = new_paragraph.split()
   for word in words:
      frequency = words.count(word)
      dict[word] = frequency
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
d = dictionary(new_paragraph, dict)

for key, value in sorted(d.items(), key=alphabetical):
  print(f"{key} : {value}")
