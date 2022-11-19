#!/usr/bin/env python3

# In module mp3collection_v2_131.py extend the MP3Collection class to support track
# lookup by artist i.e. add a method get_mp3s_by_artist() that returns a list of all tracks by the given artist.
# You must include in mp3collection_v2_131.py a copy of your MP3Track class definition from mp3track_v2_131.py.
# When your class is correctly implemented, running the following program should produce no output.

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

class MP3Collection(object):

    def __init__(self):
        self.collection = {}

    def add(self, track):
        self.collection[track.title] = track

    def remove(self, track):
        del self.collection[track]

    def get_mp3s_by_artist(self, artist):
        track = []
        for v in self.collection.values():
            if artist in v.artist:
                track.append(v)  # track.append(v.title) gives titles of songs
        return track

    def lookup(self, track):
        if track in self.collection:
            return self.collection[track]
        else:
            return None
