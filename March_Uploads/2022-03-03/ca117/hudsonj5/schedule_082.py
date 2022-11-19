#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02} ({self.duration} minutes)"

class Schedule(object):

    def __init__(self):
        self.meeting = {}

    def add(self, m):
        self.meeting[m.hour] = m

    def __str__(self):
        schedule = []
        schedule.append("Schedule")
        schedule.append("--------")
        for k, v in sorted(self.meeting.items()):
            schedule.append(f"{v}")
        schedule.append(f"Meetings today: {len(self.meeting)}")
        return "\n".join(schedule)
