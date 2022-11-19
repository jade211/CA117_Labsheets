#!/usr/bin/env python3

import sys

for sentence in sys.stdin:
   s = sentence.strip()
   if s[-2:] in ["ch", "sh"]:
      print(s + "es")
   elif s[-1:] in ["x", "s", "z"]:
      print(s + "es")
   elif s[-2] in "bcdfghjklmnpqrstvwyz" and s[-1] == "y":
      print(s[:len(s) - 1] + "ies")
   elif s[-2:] == "fe":
      print(s[: len(s) - 2] + "ves")
   elif s[-1] == "f":
      print(s[: len(s) - 1] + "ves")
   elif s[-1] == "o":
      print(s + "es")
   else:
      print(s + "s")
