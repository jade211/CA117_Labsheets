#!/usr/bin/env python3

import sys
input = sys.stdin.readlines()
list = []
e_number = ""

def shortest(vowels):
   if vowels == []:
      return []
   else:
      shortest = vowels[0]
      i = 0
      while i < len(vowels):
         if len(vowels[i]) < len(shortest):
            shortest = vowels[i]
         i = i + 1
   return shortest

def iary(list):
   for word in list:
      total = 0
      end = [word for word in list if word.endswith("iary")]
      total = len(end)
   return total


for word in input:
   word = word.lower().strip()
   list.append(word)
   vowels = [word for word in list if "a" in word and "e" in word and "i" in word and "o" in word and "u" in word]
   if word.lower().count("e") >= e_number.count("e"):
      e_number = word

print(f"Shortest word containing all vowels: {shortest(vowels)}")
print(f"Words ending in iary: {iary(list)}")
print(f"Words with most e's: {e_number}")
