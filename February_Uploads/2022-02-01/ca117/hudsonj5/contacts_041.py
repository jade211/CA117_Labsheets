#!/usr/bin/env python3

import sys
file = sys.argv[1]
names = sys.stdin.readlines()

with open(file) as f:
   input = f.readlines()

def dictionary(words):
   people = words[0]
   numbers = words[1]
   dictionary = {}
   i = 0
   while i < len(words):
      dictionary[people] = numbers
      i = i + 1
   return dictionary

def look(names, dict)
   i = 0
   while i < len(names):
      if names[i].rstrip() in dict:
         print(f"Name: {names[i]}")
         print(f"Phone: {dict.values()}".strip())
      else:
         print(f|"Name: {names[i]}")
         print("No such contact")
      i = i + 1

for lines in input:
   words = lines.split()
   dict = dictionary(words)
   lookfor = look(names, dict)
print(lookfor)
