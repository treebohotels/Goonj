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


class CustomMessage(object):
    __slots__ = ['tags', 'severity', 'message', 'error', 'error_id', 'subject']

    def __init__(self, tags, severity, message, error, error_id, subject):
        self.tags = tags
        self.severity = severity
        self.message = message
        self.error = error
        self.error_id = error_id
        self.subject = subject

    def __str__(self):
        return 'tags:{} , severity:{} , message:{} , error_id:{} , error:{} , subject:{}'.format(self.tags,
                                                                                                 self.severity,
                                                                                                 self.message,
                                                                                                 self.error,
                                                                                                 self.error_id,
                                                                                                 self.subject)


class SmtpServerConfig(object):
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
