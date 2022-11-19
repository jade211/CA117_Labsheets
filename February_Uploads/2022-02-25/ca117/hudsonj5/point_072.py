#!/usr/bin/env python3

from math import sqrt

class Point(object):

   def __init__(self, x=0, y=0):
      self.x, self.y = x, y

   def distance(self, p2):
      return sqrt(((p2.x - self.x) ** 2) + ((p2.y - self.y) ** 2))

   def __str__(self):
      p = f"({self.x:.1f}, {self.y:.1f})"
      return p


# distance = √[(x₂ - x₁)² + (y₂ - y₁)²]
