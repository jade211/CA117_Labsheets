#!/usr/bin/env python3

class Lamp(object):

   def __init__(self, on=False):  # if nothing supplied, default is False
      self.on = on

   def turn_on(self):
      if self.on is False:
         self.on = True

   def turn_off(self):
      if self.on is True:
         self.on = False

   def toggle(self):
      if self.on is True:
         self.on = False
      else:
         self.on = True
    # self.on = not self.on
