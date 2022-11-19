#!/usr/bin/env python3

import sys
numbers_written = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
input = sys.stdin.readlines()

def dictionary(numbers):
   i = 0
   while i < len(numbers):
      number = numbers[i]
      if number in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
         numbers[i] = number.replace(number, numbers_written[int(number)], 1)
      else:
         numbers[i] = "unknown"
      i = i + 1
   return (" ".join(numbers))


for line in input:
   numbers = line.strip().split()
   print(dictionary(numbers))
