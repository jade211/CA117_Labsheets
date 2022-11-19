#!/usr/bin/env/python3

import sys


def compare(s):
   total = 0
   s = s.strip()
   s = s.upper()
   s = s.split()
   for letter in s[0]:
      if letter in s[1]:
         total = total + 1
         s[1] = s[1].replace(letter, "")
      else:
         total = total
   return total


for words in sys.stdin:
   s = words
   split = s.strip().upper().split()
   string = compare(s)  # print(string), print(len(split[0]))
   if string == len(split[0]):
      print("True")
   else:
      print("False")

# 2 strings being compared
# all characters in string 1 same as string2
# can only be matched once
