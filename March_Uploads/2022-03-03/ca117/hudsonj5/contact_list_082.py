#!/usr/bin/env python3

class Contact(object):
    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.phone} {self.email}"


class ContactList(object):

    def __init__(self):
        self.d = {}

    def add(self, contact):
        self.d[contact.name] = contact

    def remove(self, name):
        if name in self.d:
            del self.d[name]

    def get(self, name):
        if name in self.d:
            return self.d[name]

    def __str__(self):
        slist = []
        slist.append("Contact list")
        slist.append("------------")
        for k, v in sorted(self.d.items()):
            slist.append(f"{v}")
        return "\n".join(slist)
