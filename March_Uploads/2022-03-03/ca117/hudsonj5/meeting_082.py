#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02} ({self.duration} minutes)"
