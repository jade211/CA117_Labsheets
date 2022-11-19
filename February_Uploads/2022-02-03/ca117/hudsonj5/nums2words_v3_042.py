#!/usr/bin/env python3

import sys
numbers_written = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
irish = ["naid", "aon", "do", "tri", "ceathar", "cuig", "se", "seacht", "ocht", "naoi", "deich"]
input = sys.stdin.readlines()

def dictionary(numbers, numbers2):
   i = 0
   while i < len(numbers) and i < len(numbers2):
      number = numbers[i]
      number2 = numbers2[i]
      if number in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
         numbers[i] = number.replace(number, numbers_written[int(number)], 1)
         if number2 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            numbers2[i] = number2.replace(number2, irish[int(number2)], 1)
      else:
         numbers[i] = "unknown"
      i = i + 1
   return(" ".join(numbers2))


for line in input:
   numbers = line.strip().split()
   numbers2 = line.strip().split()
   print(dictionary(numbers, numbers2))
