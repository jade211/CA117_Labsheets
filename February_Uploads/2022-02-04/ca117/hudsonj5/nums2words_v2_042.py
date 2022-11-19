#!/usr/bin/env python3

import sys
numbers_dictionary = {"0": "zero",
                      "1": "one",
                      "2": "two",
                      "3": "three",
                      "4": "four",
                      "5": "five",
                      "6": "six",
                      "7": "seven",
                      "8": "eight",
                      "9": "nine",
                      "10": "ten"}
input = sys.stdin.readlines()

def map(numbers):
   list = []
   for number in numbers:
      if number in numbers_dictionary:
         list.append(numbers_dictionary[number])
      else:
         list.append("unknown")
   return " ".join(list)


for line in input:
   numbers = line.strip().split()
   print(map(numbers))
