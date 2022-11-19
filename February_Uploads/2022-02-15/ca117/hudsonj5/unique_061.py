#!/usr/bin/env python3

import sys

integers = sys.stdin.readlines()

def counter(number_list):
   new_list = []
   try:

      for number in number_list:
         if number_list.count(number) == 1:
            new_list.append(number)
      return max(new_list)
   except ValueError:
      return "none"


for numbers in integers:
   number_list = []
   number = numbers.strip().split()
   for n in number:
      number_list.append(n)
   print(counter(number_list))
