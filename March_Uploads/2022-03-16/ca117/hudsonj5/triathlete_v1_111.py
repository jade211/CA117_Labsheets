#!/usr/bin/env python3

class Triathlete(object):

   def __init__(self, name, id):
      self.name = name
      self.tid = id

   def __str__(self):
      info = []
      info.append(f"Name: {self.name}")
      info.append(f"ID: {self.tid}")
      return "\n".join(info)
