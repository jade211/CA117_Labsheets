#!/usr/bin/env python3

def reverse_list(s, new_list=None):
   if new_list is None:
      new_list = []
   if len(s) == 0:
      return new_list
   else:
      new_list.append(s[- 1])
   return new_list + reverse_list(s[:-1])
