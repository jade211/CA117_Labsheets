#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        info = []
        info.append(f"Title: {self.title}")
        info.append(f"Duration: {self.duration}")
        return "\n".join(info)

class MP3Collection(object):

    def __init__(self):
        self.collection = {}

    def add(self, track):
        self.collection[track.title] = track

    def remove(self, track):
        del self.collection[track]

    def lookup(self, track):
        if track in self.collection:
            return self.collection[track]
        else:
            return None
