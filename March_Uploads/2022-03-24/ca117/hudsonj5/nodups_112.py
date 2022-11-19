#!/usr/bin/env python3

import sys
import string

paragraph = sys.stdin.readlines()

# print(paragraph)  # original paragraph ****

def punct(paragraph):
   for char in string.punctuation:
      paragraph = paragraph.replace(char, "")
   return paragraph


# new_paragraph = punct(paragraph)
# w = new_paragraph.strip().lower().split()

words = []
for word in paragraph:
   word = word.strip().split()
   i = 0
   while i < len(word):
      if punct(word[i].lower()) in words:
         word[i] = "."
      else:
         words.append(punct(word[i].lower()))
      i = i + 1
   print(" ".join(word))
