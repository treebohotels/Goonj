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
        return '{"subject":"%s","message":"%s","tags":"%s","severity":"%s","error":"%s","error_id":"%s"}' \
               % (self.subject,
                  self.message,
                  self.tags,
                  self.severity,

                  self.error,
                  self.error_id,

                  )


class SmtpServerConfig(object):
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password


class AlertRuleConfig(object):
    def __init__(self, error_code, threshold, frequency=None):
        self.error_code = error_code
        self.threshold = threshold
        self.frequency = frequency
