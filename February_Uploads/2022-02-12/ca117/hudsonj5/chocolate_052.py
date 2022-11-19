#!/usr/bin/env python3

import sys

def chocbar(calories):
   total = 0
   if int(calories) > 0:
      total = total + 1
      integer_calories = int(calories) - 400
      if integer_calories / 400 > 0:
         total = total + integer_calories // 400
         if integer_calories % 400 > 0:
            total = total + 1
   return total


for calories in sys.stdin:
   intake = chocbar(calories)
   print(intake)
