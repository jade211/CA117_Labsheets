#!/usr/bin/env python3

import sys

def multiples3(n):
   numbers = range(1, n + 1)
   multiples_of_three = [n for n in numbers if n % 3 == 0]
   return multiples_of_three

def squares3(n):
   numbers = range(1, n + 1)
   squares_of_3 = [n * n for n in numbers if n % 3 == 0]
   return squares_of_3

def double4(n):
   numbers = range(1, n + 1)
   doubles_of_4 = [n * 2 for n in numbers if n % 4 == 0]
   return doubles_of_4


def multiples3_4(n):
   numbers = range(1, n + 1)
   multiples_of_3_4 = [n for n in numbers if n % 3 == 0 or n % 4 == 0]
   return multiples_of_3_4

def multiples3_and_4(n):
   numbers = range(1, n + 1)
   multiples_of_3_and_4 = [n for n in numbers if n % 3 == 0 and n % 4 == 0]
   return multiples_of_3_and_4


for n in sys.stdin:
   n = int(n)
   print(f"Multiples of 3: {multiples3(n)}")
   print(f"Multiples of 3 squared: {squares3(n)}")
   print(f"Multiples of 4 doubled: {double4(n)}")
   print(f"Multiples of 3 or 4: {multiples3_4(n)}")
   print(f"Multiples of 3 and 4: {multiples3_and_4(n)}")
