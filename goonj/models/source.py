import sqlite3


class AlertSource(object):

    def __init__(self):
        self.name = ""
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)
