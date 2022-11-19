#!/usr/bin/env python3

def count_letters(s):
   if s == "":
      return 0
   else:
      return 1 + count_letters(s[1:])  # s[1] now becomes s[0] as it runs through function again.
