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


class Circle(object):
   def __init__(self, centre=None, radius=1):
      if centre is None:
         centre = Point()  # will create a new point which will default to parameters above (x=0,y=0)
      self.centre = centre
      self.radius = radius

   def __str__(self):
      return f"Centre: {self.centre}\nRadius: {self.radius}"

   def __add__(self, other):
      centre = Point.midpoint(self.centre, other.centre)
      radius = self.radius + other.radius
      return Circle(Point(centre.x, centre.y), radius)
