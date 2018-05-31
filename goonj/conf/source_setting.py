from goonj.conf import constants
from goonj.entities import AlertSource, Severity
from goonj.exception import EmailChannelNotDefined, SlackChannelNotDefined, SourceNotInitalized, NoSevDefined, \
    SlackChannelSettingsNotDefined, EmailChannelSettingsNotDefined, SMSChannelSettingsNotDefined, SevNotSupported


class SourceSettings(object):

    def __init__(self, sources, channels_map):
        self.alert_sources = self.get_alert_sources(sources, channels_map)

    def get_alert_sources(self, sources, channels_map):
        return {key: self.initialize_alert_source(key, value, channels_map) for
                key, value in
                sources.items()}

    def initialize_alert_source(self, key, value, channels_map):
        """

        :param key: name of the source
        :param value: value of the source
        :param channels_map:

         structure of channel_map looks like below
         email_channel=
                    {'email_channle_name1':email_channel_object1,
                     'email_channle_name2':email_channel_object2}
         sms_channel=
                    {'sms_channle_name1':sms_channel_object1,
                     'sms_channle_name2':smsl_channel_object2}


        A Source will have sev's{}
        Each sev will have channels associated to it.
        Source will also have list of default channels associate with

        channel_obj can be object of email_cahnnel_obj,sms_channel_obj etc

        source={
                'high':[channel_obj1,channel_objj2,channel_obj3],
                'low' :[channle_obj2,channle_obj4]
                'default_channels':[channel_obj5]

        }

        Channels can be of multiple type email_channel,sms_channel,
        slack_channel

        """
        if not value:
            raise SourceNotInitalized('Source is not intialized ,If no sevs,channels  are associated initialize it '
                                      'with None ')

        if value == 'None':
            return AlertSource(key, None, None)

        default_channels_obj = None
        if 'default_channels' in value:
            default_channels_obj = self.get_channels(value['default_channels'],
                                                     channels_map)

        sev_obj = self.get_sev(value['sev'], channels_map)
        return AlertSource(key, default_channels_obj, sev_obj)

    def get_channels(self, channels, channels_map):
        """

      :param channels:
            channels ={
               'email_channels':['channle_name1',channel_name2],
               'slack_channels':['channle_name3',channel_name4]
               }

      :param channels_map:

      structure of channel_map looks like below
      email_channel=
                 {'email_channle_name1':email_channel_object1,
                  'email_channle_name2':email_channel_object2}
      sms_channel=
                 {'sms_channle_name1':sms_channel_object1,
                  'sms_channle_name2':smsl_channel_object2}


      :return: list of channel objects [channel_objec1  (sms_channel),
         channle_object2  (slack_channel) ,channel_object3  (sms_channel) ]
        """

        channels_obj = []

        if not channels:
            return channels_obj

        if constants.CHANNEL_SLACK in channels:

            if not (channels_map and hasattr(channels_map, 'slack_channels')):
                raise SlackChannelSettingsNotDefined(
                    'Settings for slack channel is not defined ,please define it ')

            try:
                channels_obj.extend(
                    [channels_map.slack_channels[name] for name in
                     channels[constants.CHANNEL_SLACK]])
            except KeyError as e:
                raise SlackChannelNotDefined('Slack channel \'{}\' is used but not '
                                             'defined in configuration file'
                                             ''.format(e.args[0]))
        if constants.CHANNEL_EMAIL in channels:

            if not (channels_map and hasattr(channels_map, 'email_channels')):
                raise EmailChannelSettingsNotDefined(
                    'Settings for email channel is not defined ,please define it ')

            try:
                channels_obj.extend(
                    [channels_map.email_channels[name] for name in
                     channels[constants.CHANNEL_EMAIL]])
            except KeyError as e:
                raise EmailChannelNotDefined('Email channel  \'{}\' is used but not '
                                             'defined in configuration file'
                                             ''.format(e.args[0]))
        if constants.CHANNEL_SMS in channels:

            if not (channels_map and hasattr(channels_map, 'sms_channels')):
                raise SMSChannelSettingsNotDefined(
                    'Settings for sms channel is not defined ,please define it ')
            try:
                channels_obj.extend(
                    [channels_map.sms_channels[name] for name in
                     channels[constants.CHANNEL_SMS]])
            except KeyError as e:
                raise EmailChannelNotDefined('Sms channel  \'{}\' is used but not '
                                             'defined in configuration file'
                                             ''.format(e.args[0]))

        return channels_obj

    def get_sev(self, sev, channels_map):
        """

        :param sev: sev associated with a source
        sev={
        'high':{
               'email_channels':['channle_name1',channel_name2],
               'slack_channels':['channle_name3',channel_name4]
               },
        'low':{
               'email_channels':['channle_name1',channel_name2],
               'slack_channels':['channle_name3',channel_name4]
               }
        }
        :param
        structure of channel_map looks like below
        email_channel=
                 {'email_channle_name1':email_channel_object1,
                  'email_channle_name2':email_channel_object2}
        sms_channel=
                 {'sms_channle_name1':sms_channel_object1,
                  'sms_channle_name2':smsl_channel_object2}
        :return:

        sev={
        'high':[channel_obj1,channel_objj2,channel_obj3],
        'low' :[channle_obj2,channle_obj4]
        }



        """

        if not sev:
            raise NoSevDefined('No Sevs are defined within \'sev\' in settings file ,define at least one sev ,'
                               'or remove the sev setting')

        sev_obj = {}

        for sev_name, sev_value in sev.items():
            if sev_name in constants.SEV_VALUES:
                channels_obj = self.get_channels(sev[sev_name], channels_map)
                sev_obj[sev_name] = Severity(channels_obj)
            else:
                raise SevNotSupported(
                    'Sev {} not supported valid values are low,medium,high,critical '.format(sev_name))

        return sev_obj
