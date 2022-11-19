#!/usr/bin/env python3

# Make each a list of 2
# ever first one in a lis and every second one in a list
# put both in dictionaries and print firsts in increading
# and second in decreasing

import sys
names = sys.stdin.readlines()

def len_funct(names):
   d = {}
   for name in names:
      name = name.strip()
      d[name] = len(name)
   return d

def in_order1(d):
   ordered = []
   for key, value in sorted(d.items(), key=len):
      ordered.append(f"{key}")
   return "\n".join(ordered).strip()


every_first = names[::2]
every_second = names[1::2]
every_second.reverse()

every_first_d = len_funct(every_first)
every_second_d = len_funct(every_second)

print(in_order1(every_first_d))
order2 = in_order1(every_second_d)

if order2:
    print(order2)
