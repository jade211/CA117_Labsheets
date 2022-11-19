#!/usr/bin/env python3

import sys
file = sys.argv[1]
names = sys.stdin.readlines()

def dictionary(input):
   dictionary = {}
   with open(file) as f:
      input = f.readlines()
      for words in input:
         words = words.split()
         people = words[0]
         numbers = words[1]
         i = 0
         while i < len(input):
            dictionary[people] = numbers
            i = i + 1
   return dictionary

def look(name):
   if name in dict:
      print(f"Name: {name}")
      return (f"Phone: {dict[name]}")
   elif name not in dict:
      print(f"Name: {name}")
      return (f"No such contact")


dict = dictionary(file)
for name in names:
   lookfor = look(name.strip())
   print(lookfor)
