#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
number_order = []

def ordered(numbers):
   data = numbers.strip()
   data = data.split()
   #data = data.replace(" ", "")
   #data = data.split()
   data = sorted(data)
   A = data[0]
   B = data[1]
   C = data[2]
   return A, B, C

numbers = ordered(lines[0])
#print(numbers)

for letter in lines[1]:
   if letter == "A":
      number_order.append(numbers[0])
   elif letter == "B":
      number_order.append(numbers[1])
   elif letter == "C":
      number_order.append(numbers[2])

print(" ".join(number_order))



#print(ordered1)
#print(ordered2)
#ordered2[0] = ordered1[0]
#ordered2[1] = ordered1[1]
#ordered2[2] = ordered1[2]
#print(ordered1, ordered2)
#print(abc)

#dict[ordered2[0]] = ordered1[0]
#dict[ordered2[1]] = ordered1[1]
#dict[ordered2[2]] = ordered1[2]
#print(ordered1, ordered2)
#print(dict)

#i = 0
#while i < len(lines[1]):
#for input in lines[1]:
   #if lines[1][i] in ordered1:
      #print("yes")
   #i = i + 1
