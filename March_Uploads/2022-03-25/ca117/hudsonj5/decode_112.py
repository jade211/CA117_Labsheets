#!/usr/bin/env python3

import sys

vowels = ["a", "e", "i", "o", "u"]

# After each vowel he adds a p followed by the vowel again.
# Write a program called decode_112.py that decodes Jimmy’s messages.
# Eg: papa = pa(pa)pa(pa)

def vowel_funct(word):
   correct = []
   i = 0
   while i < len(word):
      if word[i] in vowels:
         word = word.replace(word[i:i + 3], word[i])
      i = i + 1
   return word


for word in sys.stdin:
   print(vowel_funct(word.strip()))
