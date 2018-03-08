
class AlertSource(object):
    def __init__(self, name, default_channels, severity):
        self.name = name
        self.default_channels = default_channels
        self.severity = severity


class Severity(object):
    def __init__(self, channels):
        self.channels = channels


class Tag(object):
    def __init__(self, name):
        self.name = name
