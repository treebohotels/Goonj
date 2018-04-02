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

    def warn(self, sev, message, subject=None, error_id=None, error=None,
             tag_list=None, *args, **kwargs):
        custom_message = CustomMessage(
            tag_list, sev.value, message, error, error_id)

        if self.logger is not None:
            self.logger.warn(custom_message, args, kwargs)
        self.__alert(sev, message, subject, error_id, error,
                     tag_list)

    def info(self, sev, message, subject=None, error_id=None, error=None,
             tag_list=None, *args, **kwargs):

        custom_message = CustomMessage(
            tag_list, sev.value, message, error, error_id, subject)
        if self.logger is not None:
            self.logger.info(custom_message, args, kwargs)
        self.__alert(sev, message, subject, error_id, error,
                     tag_list)

    def error(self, sev, message, subject=None, error_id=None, error=None,
              tag_list=None, *args, **kwargs):
        custom_message = CustomMessage(
            tag_list, sev.value, message, error, error_id, subject)
        if self.logger is not None:
            self.logger.error(custom_message, args, kwargs)
        self.__alert(sev, message, subject, error_id, error,
                     tag_list)

    def debug(self, sev, message, subject=None, error_id=None, error=None,
              tag_list=None, *args, **kwargs):
        custom_message = CustomMessage(
            tag_list, sev.value, message, error, error_id, subject)
        if self.logger is not None:
            self.logger.debug(custom_message, args, kwargs)
        self.__alert(sev, message, subject, error_id, error,
                     tag_list)

    def exception(self, sev, message, subject=None, error_id=None, error=None,
                  tag_list=None, *args, **kwargs):
        custom_message = CustomMessage(
            tag_list, sev.value, message, error, error_id, subject)
        if self.logger is not None:
            self.logger.exception(custom_message, args, kwargs)
        self.__alert(sev, message, subject, error_id, error,
                     tag_list)

    def __alert(self, sev, message, subject, error_id, error,
                tag_list):

        if sev is None:  # If no Sev level is defined with alert it will just
            # act as logging , TODO check this beahviour how it
            # shoould
            #  work
            return
        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

            for channel in self.source.default_channels:
                channel.send(sev, message, subject, error_id, error,
                             tag_list)

        try:
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
