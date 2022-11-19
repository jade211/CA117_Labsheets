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

class MP3Collection(object):

    def __init__(self, collection=None):
        if collection is None:
            self.collection = {}
        else:
            self.collection = collection

    def add(self, track):
        self.collection[track.title] = track

    def __add__(self, other):
        new = dict(self.collection, **other.collection)
        # new = self.collection | other.collection
        return MP3Collection(new)

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
