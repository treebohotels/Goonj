from goonj.conf.constants import Sev


class SmartAlert(object):

    def __init__(self, name, source, logger=None):
        """

        :param name: name of the source
        :param source:  value of the source
        :param logger: logger object used for general logging
        """
        self.source = source
        self.name = name
        self.logger = logger

    def warn(self, sev, message, subject, error_id, error,
             tag_list, *args, **kwargs):

        if self.logger is not None:
            self.logger.warn(message, args, kwargs)
        self.alert(sev, message, subject, error_id, error,
                   tag_list)

    def info(self, sev, message, subject, error_id, error,
             tag_list, *args, **kwargs):

        if self.logger is not None:
            self.logger.info(message, args, kwargs)
        self.alert(sev, message, subject, error_id, error,
                   tag_list)

    def error(self, sev, message, subject, error_id, error,
              tag_list, *args, **kwargs):
        if self.logger is not None:
            self.logger.error(message, args, kwargs)
        self.alert(sev, message, subject, error_id, error,
                   tag_list)

    def debug(self, sev, message, subject, error_id, error,
              tag_list, *args, **kwargs):
        if self.logger is not None:
            self.logger.debug(message, args, kwargs)
        self.alert(sev, message, subject, error_id, error,
                   tag_list)

    def exception(self, sev, message, subject, error_id, error,
                  tag_list, *args, **kwargs):
        if self.logger is not None:
            self.logger.exception(message, args, kwargs)
        self.alert(sev, message, subject, error_id, error,
                   tag_list)

    def alert(self, sev, message, subject=None, error_id=None, error=None,
              tag_list=None):

        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

        for channel in self.source.default_channels:
            channel.send(sev, message, subject, error_id, error,
                         tag_list)

        for channel in self.source.severity[sev.value].channels:
            channel.send(sev, message, subject, error_id, error,
                         tag_list)
