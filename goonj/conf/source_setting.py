from goonj.channels import constants
from goonj.conf.constants import Sev
from goonj.entities import AlertSource, Severity
from goonj.exception import EmailChannelNotDefined, SlackChannelNotDefined


class SourceSettings(object):

    def __init__(self, sources, channels):
        self.alert_sources = self.get_alert_sources(sources, channels)

    def get_alert_sources(self, sources, channels_map):
        return {key: self.initialize_alert_source(key, value, channels_map) for
                key, value in
                sources.items()}

    def initialize_alert_source(self, key, value, channels_map):
        """

        :param key: name of the source
        :param value: value of the source
        :param channels_map: {'channel_type',{'channel_name','channel_object'}
        :return: intializes alert_Source

        A Source will have sev's{}
        Each sev will have channels associated to it.
        Source will also have list of default channels associate with

        source->Sev->channels
        source->default_channels->[channels]

        Channels can be of multiple type email_channel,sms_channel,
        slack_channel
        """
        default_channels_obj = None
        if 'default_channels' in value:
            default_channels_obj = self.get_channels(value['default_channels'],
                                                     channels_map)

        sev_obj = self.get_sev(value['sev'], channels_map)
        return AlertSource(key, default_channels_obj, sev_obj)

    def get_channels(self, channels, channels_map):
        """

        :param channels: map of {type of channels , [list of names of channels]}

        :param channels_map: {'channel_type',{'name','channel_object'}
        :return:   list of channel objects
        """
        channels_obj = []
        if constants.CHANNEL_SLACK in channels:

            try:
                channels_obj.extend(
                    [channels_map.slack_channels[name] for name in
                     channels[constants.CHANNEL_SLACK]])
            except KeyError as e:
                raise SlackChannelNotDefined('Slack channel \'{}\' is not '
                                             'defined in configuration file'
                                             ''.format(e.args[0]))
        if constants.CHANNEL_EMAIL in channels:
            try:
                channels_obj.extend(
                    [channels_map.email_channels[name] for name in
                     channels[constants.CHANNEL_EMAIL]])
            except KeyError as e:
                raise EmailChannelNotDefined('Email channel \'{}\' is not '
                                             'defined in configuration file'
                                             ''.format(e.args[0]))
        if constants.CHANNEL_SMS in channels:
            try:
                channels_obj.extend(
                    [channels_map.sms_channels[name] for name in
                     channels[constants.CHANNEL_SMS]])
            except KeyError as e:
                raise EmailChannelNotDefined('Sms channel \'{}\' is not '
                                             'defined in configuration file'
                                             ''.format(e.args[0]))

        return channels_obj

    def get_sev(self, sev, channels_map):
        """

        :param sev: sev associated with a source
        :param channels_map:{'channel_type',{'name_of_the_channel',
        'channel_object'}
        :return: map of {sev_name , list of channel objects associated with
        each sev}
        """
        sev_obj = {}
        if Sev.LOW.value in sev:
            channels_obj = self.get_channels(sev[Sev.LOW.value], channels_map)
            sev_obj[Sev.LOW.value] = Severity(channels_obj)

        if Sev.MEDIUM.value in sev:
            channels_obj = self.get_channels(sev[Sev.MEDIUM.value],
                                             channels_map)
            sev_obj[Sev.MEDIUM.value] = Severity(channels_obj)

        if Sev.HIGH.value in sev:
            channels_obj = self.get_channels(sev[Sev.HIGH.value], channels_map)
            sev_obj[Sev.HIGH.value] = Severity(channels_obj)

        if Sev.CRITICAL.value in sev:
            channels_obj = self.get_channels(sev[Sev.CRITICAL.value],
                                             channels_map)
            sev_obj[Sev.CRITICAL.value] = Severity(channels_obj)

        return sev_obj
