#!/usr/bin/env python3

class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.times = {}

   def __str__(self):
      r = []
      r.append('Name: {:s}'.format(self.name))
      r.append('ID: {:d}'.format(self.tid))
      r.append('Race time: {:d}'.format(self.total_time()))  # could do self.time(run) + cycle + etc)
      return '\n'.join(r)

   def total_time(self):
      if not self.times:  # if nothing recorded, returns 0
         return 0
    # return sum([t for t in self.times.values()])
      return sum(self.times.values())

   def add_time(self, d, t):  # d means discipline, t is time
    # d 'cycle'
    # t 100
    # self.times['cycle'] = 100
      self.times[d] = t

   def get_time(self, d):
     if d in self.times:
        return self.times[d]
     else:
        return None
