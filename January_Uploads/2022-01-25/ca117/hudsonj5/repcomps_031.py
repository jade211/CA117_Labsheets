#!/usr/bin/env python3

import sys
list = []

def multiples3(n):
   list = []
   numbers = range(1, n + 1)
   normal = [int(n) for n in numbers]
   multiples_of_three = [int(n) for n in numbers if n % 3 == 0]
   i = 0
   while i < len(normal):
      if normal[i] in multiples_of_three:
         list.append("X")
      else:
         list.append(normal[i])
      i = i + 1
   return list


for n in sys.stdin:
   n = int(n)
   print(f"Multiples of 3 replaced: {multiples3(n)}")
