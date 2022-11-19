#!/usr/bin/env python3

import sys

def primes(n):
   n = int(n)
   if n <= 1:
      return False
   for numbers in range(2, n // 2 + 1):
      if n % numbers == 0:
         return False
   return True


def primetrue(numbers):
    return [n for n in numbers if primes(n) is True]


for n in sys.stdin:
   numbers = range(1, int(n) + 1)
   print(f"Primes: {primetrue(numbers)}")
