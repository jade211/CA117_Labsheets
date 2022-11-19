#!/usr/bin/env python3

class Student(object):

   def __init__(self, sid, name, modules=None):
      self.sid = sid
      self.name = name
      self.modlist = [] if modules is None else modules

   def add_module(self, module):
      if module not in self.modlist:
         self.modlist.append(module)

   def del_module(self, module):
      if module in self.modlist:
         self.moodlist.remove(module)

   def __str__(self):
      info = []
      info.append(f"ID: {self.sid}")
      info.append(f"Name: {self.name}")
      info.append(f"Modules: {', '.join(self.modlist)}")
      return "\n".join(info)
