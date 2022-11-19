#!/usr/bin/env python3

def minimum(n):
   if len(n) == 1:  # base case
      return n[0]
   if n[1] < n[0]:
      del(n[0])
   else:
      del(n[1])
   return minimum(n)
