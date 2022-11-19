#!/usr/bin/env python3

import sys
from math import sqrt

def roots(a, b, c):
   try:
      r1 = (- b + sqrt((b ** 2) - ((a * c) * 4))) / (2 * a)
      r2 = (- b - sqrt((b ** 2) - ((a * c) * 4))) / (2 * a)
      return (f"r1 = {r1}, r2 = {r2}")
   except ValueError:
      return None


for abc in sys.stdin:
   abc = abc.strip().split()
   a, b, c = abc
   print(roots(int(a), int(b), int(c)))
