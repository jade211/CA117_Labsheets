#!/usr/bin/env python3

import sys
rank = []
biggest = 0

for group in sys.stdin:
   cards = group.strip().split()
   for card in cards:
      rank.append(card[0])
for amount in rank:
   number = rank.count(amount)
   if number > biggest:
      biggest = number
print(biggest)
