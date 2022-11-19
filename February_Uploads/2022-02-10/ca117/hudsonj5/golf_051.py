#!/usr/bin/env python3

import sys

def increasing_order(value):
   return value[1]


list = []
dict = {}
for input in sys.stdin:
   total = 0
   input = input.strip().split()
   name = input[:len(input) - 3]
   name = " ".join(name)
   goal = input[len(input) - 3:]
   goal_correct = "".join(goal)
   goals_confirmed = ""
   for character in goal_correct:
      if character.isdigit() is False:
         list.append(name)
      else:
         goals_confirmed = goals_confirmed + " " + character
   goals_confirmed = goals_confirmed.split()
   for integer in goals_confirmed:
      integer = int(integer)
      total = integer + total
   dict[name] = total
for name in list:
   if name in dict:
      dict.pop(name)

for key, value in sorted(dict.items(), key=increasing_order):
   print(f"{key}: {value}")
if len(list) > 0:
   print(f"Disqualified: {', '.join(list)}")
