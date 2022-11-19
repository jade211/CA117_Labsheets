#!/usr/bin/env python3

def factorial(n):
   if n == 0:  # base case
      return 1
   return n * factorial(n - 1)


# 1 = 1
# 2 = 2
# 3 = 6
# 4 = 24
# 5 = 120
# 6 = 720
# 7 = 5040
