#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artist=None):
        self.title = title
        self.duration = duration
        if artist is None:
            self.artist = []
        else:
            self.artist = artist

    def add_artist(self, artist):
        self.artist.append(artist)

    def __str__(self):
        info = []
        info.append(f"Title: {self.title}")
        singers = ", ".join(self.artist)
        info.append(f"By: {singers}")
        info.append(f"Duration: {self.duration}")
        return "\n".join(info)
