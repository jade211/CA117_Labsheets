#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
d = {}

def increasing_order(value):
   return value[1]

def sales_numbers(name, sales):
   total = 0
   if len(sales) > 1:
      for sale in sales:
         total = total + int(sale)
   elif len(sales) == 1:
      for sale in sales:
         total = total + int(sale)
   result = total / len(sales)
   d[name] = result
   return d


for line in lines:
   line = line.strip().split(":")
   name, sales = line[0].strip(), line[1].strip().split(",")
   dictionary_sales = sales_numbers(name, sales)

for key, value in sorted(dictionary_sales.items(), key=increasing_order, reverse=True):
   print(f"{key}: {value:.2f}")
