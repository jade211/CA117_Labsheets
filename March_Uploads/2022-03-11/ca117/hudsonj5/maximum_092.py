#!/usr/bin/env python3

def maximum(n):
   if len(n) == 1:  # base case
      return n[0]
   if n[1] > n[0]:
      del(n[0])
   else:
      del(n[1])
   return maximum(n)


# bigger of 1 and biggest in remainder
# example case = maximum([6,5,1,3,4]).
# sends list through function and if list only has one number, that one number gets returned and is the largest.
# if list has more than one, compares first number with second.
# if first is bigger, second (n[1]) gets removed.
# if second is bigger, n[0] gets removed.
# puts newly edited list through function again and does same process till list has been ran through.
# by then the list will only contain one element (the largest) and will return at if len(n) == 1.
