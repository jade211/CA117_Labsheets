#!/usr/bin/env python3

import sys
numbers_written = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
input = sys.stdin.readlines()
d = {}

def dictionary(d, numbers, numbers_written):
   for number in numbers:
      i = 0
      while i < len(numbers_written):
         written = numbers_written[i]
         if int(number) == i:
            d[number] = written
         i = i + 1
   return d

def list(numbers):
   list = []
   for number in numbers:
      if number in dict:
         list.append(dict[number])
   return " ".join(list)


for line in input:
   numbers = line.strip().split()
   dict = dictionary(d, numbers, numbers_written)
   print(list(numbers))
