#!/usr/bin/env python3

import sys
dict_book = {}

def calculations(dict_book, new_string):
   num = dict_book[new_string[0]]
   try:

      i = 0
      while i < len(new_string):
         if new_string[i] == "+":
            num = num + dict_book[new_string[i + 1]]
         elif new_string[i] == "-":
            num = num - dict_book[new_string[i + 1]]
         i = i + 1
         word = [key for key, value in dict_book.items() if value == num]
         if len(word) == 0:
            word = "unknown"
      return " ".join(new_string) + " " + "".join(word)
   except KeyError:
     return " ".join(new_string) + " " + "unknown"


for input_line in sys.stdin:
   input_values = input_line.strip().split()
   command = input_values[0]
   if "def" in command:
      dict_book[input_values[1]] = int(input_values[2])
   if "calc" in command:
      new_string = input_values[1:]
      result = calculations(dict_book, new_string)
      print(result)
   if "clear" in command:
      dict_book = {}
