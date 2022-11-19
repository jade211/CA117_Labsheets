#!/usr/bin/env python3

import sys
english_dictionary = {"0": "zero",
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

english_irish = sys.argv[1]
with open(english_irish) as f:
   file = f.readlines()
   dict = {}
   for lines in file:
      words = lines.split()
      dict[words[0].strip()] = words[1].strip()

def map(numbers, dict):
   list = []
   list1 = []
   for number in numbers:  # 1
      if number in english_dictionary:  # 1
         for english in dict:  # one
            if english in english_dictionary[number]:  # if one in dictionary at position 1
               list.append(dict[english])  # prints out one value from dict, which is aon
      else:
         list.append("unknown")
   return list


for line in input:
   numbers = line.strip().split()
   list = map(numbers, dict)
   print(" ".join(list))
