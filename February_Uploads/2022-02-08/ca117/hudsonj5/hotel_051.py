#!/usr/bin/env python3

import sys
input = sys.stdin.readline().strip().split()
num_of_rooms = int(input[0])
occupied = input[1:]
all_rooms = list(range(1, num_of_rooms))

for room in occupied:
   room = int(room)
   for number in all_rooms:
      if number == room:
         all_rooms.remove(room)

if len(all_rooms) > 0:
   print(all_rooms[0])
else:
   print("no room")
