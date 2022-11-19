#!/usr/bin/env python3

import sys
file = sys.argv[1]
names = sys.stdin.readlines()

def dictionary(input):
   dictionary_numbers = {}
   dictionary_emails = {}
   with open(file) as f:
      input = f.readlines()
      for words in input:
         words = words.split()
         people = words[0]
         numbers = words[1]
         emails = words[2]
         i = 0
         while i < len(input):
            dictionary_numbers[people] = numbers
            dictionary_emails[people] = emails
            i = i + 1
   return dictionary_numbers, dictionary_emails

def look(name):
   if name in dict1 and name in dict2:
      print(f"Name: {name}")
      print(f"Phone: {dict1[name]}")
      return (f"Email: {dict2[name]}")
   elif name not in dict1 and name not in dict2:
      print(f"Name: {name}")
      return (f"No such contact")


dict1, dict2 = dictionary(file)
for name in names:
   lookfor = look(name.strip())
   print(lookfor)
