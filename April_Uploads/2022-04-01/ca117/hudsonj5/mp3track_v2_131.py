#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artist=None):
        self.title = title
        self.duration = duration
        if artist is None:
            self.artist = ""
        else:
            artist = ", ".join(artist)
            self.artist = artist

    def __str__(self):
        info = []
        info.append(f"Title: {self.title}")
        info.append(f"By: {self.artist}")
        info.append(f"Duration: {self.duration}")
        return "\n".join(info)
