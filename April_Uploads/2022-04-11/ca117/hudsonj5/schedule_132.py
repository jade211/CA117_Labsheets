#!/usr/bin/env python3

import sys
import string

def tagger(items):
    return int(items[1][0])


def earliest(timebook):
    times = []
    for k, v in sorted(timebook.items(), key=tagger):
        times.append(f"{k}")
    return times


timebook = {}
for times in sys.stdin:
    time_listing = []
    times = times.strip()
    time = times.strip().split()
    time_h_m = time[0]
    time_h_m = time_h_m.split(":")

    hour = time_h_m[0]
    minute = time_h_m[1]
    time_type = time[1]
    for char in time_type:
        if char in string.punctuation:
            time_type = time_type.replace(char, "")
    time_listing.append(hour)
    time_listing.append(minute)
    time_listing.append(time_type)
    if time_listing[2] == "pm":
        time_listing[0] = 12 + int(time_listing[0])
    elif time_listing[2] == "am" and time_listing[0] == "12":
        time_listing[0] = "0"
    timebook[times] = time_listing

# print(timebook)
print("\n".join(earliest(timebook)))
