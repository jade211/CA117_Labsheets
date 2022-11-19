#!/usr/bin/env python3

def alphabetical(v):
   return v.name


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

   def __str__(self):
      info = []
      for v in sorted(self.triathlon.values(), key=alphabetical):
         info.append(f"{v}")
      return "\n".join(info)
