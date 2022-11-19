#!/usr/bin/env python3

from math import sqrt
def overlap(x1=0, y1=0, r1=0, x2=0, y2=0, r2=1):
   if sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))) < r1 + r2:
      return True
   return False


# distance = √[(x₂ - x₁)² + (y₂ - y₁)²]
