#!/usr/bin/env python3

def fibonacci(n):
   if n <= 1:
      return 1
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)
