class AlertSource(object):
    def __init__(self, name,default_channels,severity):
        self.name = name
        self.default_channels = default_channels
        self.severity = severity

    def add_default_channels(self):
        pass

    def remove_default_channels(self):
        pass


class Sev(object):
    def __init__(self, channels):
        self.channels = channels

    def add_channel(self, channel):
        if self.channels is None:
            self.channels = []

        self.channels.append(channel)


class HighSev(Sev):
    pass


class LowSev(Sev):
    pass


class MediumSev(Sev):
    pass


class CriticalSev(Sev):
    pass


class Recipient(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.name == other.name and self.type == other.type

    def __hash__(self):
        return hash(self.type) + hash(self.name)


class Tag(object):

    def __init__(self, name):
        self.name = name
