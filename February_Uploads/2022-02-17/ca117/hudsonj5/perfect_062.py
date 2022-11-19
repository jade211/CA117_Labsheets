#!/usr/bin/env python3

import sys

def sum_factors(number):
   factors = [n for n in range(1, number) if number % n == 0]
   return sum(factors)

def is_perfect(added, number):
   if added == number:
      return True
   return False

def main():
   for number in sys.stdin:
      number = int(number.strip())
      #added = sum_factors(number)
      result = is_perfect(sum_factors(number), number)
      print(result)


if __name__ == '__main__':
   main()
