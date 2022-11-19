#!/usr/bin/env python3

import sys
input = sys.stdin.readlines()

def abc(numbers, letters):
   numbers = numbers.strip()
   data = numbers.split()
   data[0], data[1], data[2] = int(data[0]), int(data[1]), int(data[2])
   sort = sorted(data)
   A = str(sort[0])
   B = str(sort[1])
   C = str(sort[2])
   number_order = []
   for letter in letters:
      if letter == "A":
         number_order.append(A)
      elif letter == "B":
         number_order.append(B)
      elif letter == "C":
         number_order.append(C)
   return number_order


number_order = abc(input[0], input[1])
print(" ".join(number_order).strip())
