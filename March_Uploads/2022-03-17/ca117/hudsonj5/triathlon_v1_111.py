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

class Triathlon(object):
   def __init__(self):
      self.triathlon = {}

   def add(self, athlete):
      self.triathlon[athlete.tid] = athlete

   def remove(self, id):
      if id in self.triathlon:
         self.triathlon.pop(id)

   def lookup(self, id):
      if id in self.triathlon:
         return self.triathlon[id]
