#!/usr/bin/env python3

import sys
input = sys.stdin.readlines()
list = []

def allvowels(word):
   return "a" in word and "e" in word and "i" in word and "o" in word and "u" in word

def e_word(list):
   count = 0
   for word in list:
      if count < word.lower().count("e"):
         count = word.lower().count("e")
   return [word for word in list if word.count("e") == count]


for word in input:
   word = word.strip()
   list.append(word)


print(f"Shortest word containing all vowels: {(min([word.strip() for word in input if allvowels(word.lower())], key=len))}")
print(f"Words ending in iary: {len([word for word in list if word.lower().endswith('iary')])}")
print(f"Words with most e's: {e_word(list)}")
