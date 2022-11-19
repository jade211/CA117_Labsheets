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

   def __gt__(self, other=None):
      return self.racetime > other.racetime

   def __lt__(self, other):
      return self.racetime < other.racetime

   def __str__(self):
      info = []
      info.append(f"Name: {self.name}")
      info.append(f"ID: {self.tid}")
      info.append(f"Race time: {self.racetime}")
      return "\n".join(info)


class Triathlon(object):
   def __init__(self):
      self.triathlon = {}

   def add(self, athlete):
      self.triathlon[athlete.tid] = athlete

   def best(self):
      return min(self.triathlon.values())

   def worst(self):
      return max(self.triathlon.values())


def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())


if __name__ == '__main__':
   main()
