#!/usr/bin/env python3

import sys

def anagram(s):
   total = 0
   s = s.strip()
   s = s.upper()
   s = s.split()
   for letter in s[0]:
      if letter in s[1]:
         total = total + 1
         s[1] = s[1].replace(letter, "", 1)
      else:
         total = total
   return total


for words in sys.stdin:
   s = words
   word_compare = s.strip().upper().split()
   anagram_word = anagram(s)
   if anagram_word == len(word_compare[1]) and anagram_word == len(word_compare[0]):
      print("True")
   else:
      print("False")
