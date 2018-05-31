from goonj.conf.constants import Sev
from goonj.entities import CustomMessage


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

    def warn(self, message, sev=None, subject=None, error_id=None, error=None,
             tag_list=None, *args, **kwargs):
        self.log_message('warn', message, sev, subject, error_id, error,
                         tag_list, *args, **kwargs)

    def info(self, message, sev=None, subject=None, error_id=None, error=None,
             tag_list=None, *args, **kwargs):
        self.log_and_alert_message('info', message, sev, subject, error_id, error,
                                   tag_list, *args, **kwargs)

    def error(self, message, sev=None, subject=None, error_id=None, error=None,
              tag_list=None, *args, **kwargs):
        self.log_and_alert_message('error', message, sev, subject, error_id, error,
                                   tag_list, *args, **kwargs)

    def debug(self, message, sev=None, subject=None, error_id=None, error=None,
              tag_list=None, *args, **kwargs):
        self.log_and_alert_message('debug', message, sev, subject, error_id, error,
                                   tag_list, *args, **kwargs)

    def exception(self, message, sev=None, subject=None, error_id=None, error=None,
                  tag_list=None, *args, **kwargs):
        self.log_and_alert_message('exception', message, sev, subject, error_id, error,

                                   tag_list, *args, **kwargs)

    def log_and_alert_message(self, function_name, message, sev=None, subject=None, error_id=None, error=None,
                              tag_list=None, *args, **kwargs):
        if self.logger is not None:

            if sev is None:
                sev_value = 'No Sev'
            else:
                sev_value = sev.value
            custom_message = CustomMessage(tag_list, sev_value, message, error, error_id, subject)
            getattr(self.logger, function_name)(custom_message, *args, **kwargs)
        self.__alert(sev, message, subject, error_id, error, tag_list)

    def __alert(self, sev, message, subject, error_id, error, tag_list):

        if not sev:
            return

        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

            for channel in self.source.default_channels:
                channel.send(sev, message, subject, error_id, error,
                             tag_list)

        try:
            if self.source.severity:
                severity = self.source.severity[sev.value]
                for channel in severity.channels:
                    channel.send(sev, message, subject, error_id, error,
                                 tag_list)
        except KeyError as e:
            pass
            # Can supresss this excpetion need to check behaviour
            # raise ChannelsNotDefinedForSev('Channels are not defined for {} '
            #                                'sev in config file'
            #                                ''.format(sev.value))
