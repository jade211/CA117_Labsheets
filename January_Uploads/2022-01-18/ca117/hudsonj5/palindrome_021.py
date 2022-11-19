#!/usr/bin/env python3

import sys

def palindrome(s):
   new_string = ""
   s = s.lower()
   s = s.strip()
   for char in s:
      if char.isalnum():
         new_string = new_string + char
   return new_string


for sentence in sys.stdin:
   sentence = sentence
   words = palindrome(sentence)
   if words[0:] == words[:: -1]:
      print("True")
   else:
      print("False")
