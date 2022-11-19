#!/usr/bin/env python3

import sys
numbers_written = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
input = sys.stdin.readlines()

def dictionary(numbers):
   i = 0
   while i < len(numbers):
      number = numbers[i]
      numbers[i] = number.replace(number, numbers_written[int(number)], 1)
      i = i + 1
   return(" ".join(numbers))


for line in input:
   numbers = line.strip().split()
   print(dictionary(numbers))
