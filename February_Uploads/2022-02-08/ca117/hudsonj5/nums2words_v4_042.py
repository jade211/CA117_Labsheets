#!/usr/bin/env python3

import sys
all_numbers = {"0": "zero",
               "1": "one",
               "2": "two",
               "3": "three",
               "4": "four",
               "5": "five",
               "6": "six",
               "7": "seven",
               "8": "eight",
               "9": "nine",
               "10": "ten",
               "11": "eleven",
               "12": "twelve",
               "13": "thirteen",
               "14": "fourteen",
               "15": "fifteen",
               "16": "sixteen",
               "17": "seventeen",
               "18": "eighteen",
               "19": "nineteen",
               "20": "twenty",
               "30": "thirty",
               "40": "forty",
               "50": "fifty",
               "60": "sixty",
               "70": "seventy",
               "80": "eighty",
               "90": "ninety",
               "100": "one hundred"}

input = sys.stdin.readlines()
d = {}


def map(numbers):
   list = []
   for number in numbers:
      if str(number) in all_numbers:
         list.append(all_numbers[number])
      else:
         digits = number.split()
         for d in digits:
            new_digit = ""
            digit = str(d[0]) + "0"
            if digit in all_numbers:
               new_digit = new_digit + all_numbers[digit]
               if d[1] in all_numbers:
                  new_digit = new_digit + "-" + all_numbers[d[1]]
            list.append(new_digit)
   return " ".join(list)


for line in input:
   numbers = line.strip().split()
   print(map(numbers))
