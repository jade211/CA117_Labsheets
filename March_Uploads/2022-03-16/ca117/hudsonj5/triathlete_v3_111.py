#!/usr/bin/env python3

class Triathlete(object):

   def __init__(self, name=None, id=None, racetime=0):
      self.name = name
      self.tid = id
      self.times = {"cycle": 0, "run": 0, "swim": 0}
      self.racetime = racetime

   def add_time(self, sport, time):
      self.times[sport] = time
      self.racetime += time

   def get_time(self, sport):
      if sport in self.times:
         return self.times[sport]

   def __eq__(self, other):
      return self.racetime == other.racetime

   def __gt__(self, other):
      return self.racetime > other.racetime

   def __lt__(self, other):
      return self.racetime < other.racetime

   def __str__(self):
      info = []
      info.append(f"Name: {self.name}")
      info.append(f"ID: {self.tid}")
      info.append(f"Race time: {self.racetime}")
      return "\n".join(info)
