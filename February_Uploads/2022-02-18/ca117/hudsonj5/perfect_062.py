#!/usr/bin/env python3

import sys

def sum_factors(number):
   return sum([n for n in range(1, (number // 2) + 1) if number % n == 0])

def is_perfect(factors, number):
   return number == factors


for number in sys.stdin:
   number = int(number.strip())
   factors = sum_factors(number)
   print(is_perfect(factors, number))
