#!/usr/bin/env python3

class Point(object):

   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def midpoint(self, other):
      x_midpoint = (self.x + other.x) / 2
      y_midpoint = (self.y + other.y) / 2
      return Point(x_midpoint, y_midpoint)

   def __str__(self):
      return f"({self.x:.1f}, {self.y:.1f})"
