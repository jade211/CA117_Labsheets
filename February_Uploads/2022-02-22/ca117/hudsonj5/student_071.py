#!/usr/bin/env python3

class Student(object):

   def set_attributes(self, id_num, name, modules):
      self.name = name
      self.sid = id_num
      self.modlist = modules

   def print_attributes(self):
      print(f"ID: {self.sid}")
      print(f"Name: {self.name}")
      print("Modules: " + ', '.join(self.modlist))

   def add_module(self, mod):
      self.modlist.append(mod)

   def del_module(self, mod):
      self.modlist.remove(mod)
