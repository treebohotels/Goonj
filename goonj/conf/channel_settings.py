from goonj.channels import constants
from goonj.channels.email_channel import EmailChannel
from goonj.channels.slack_channel import SlackChannel
from goonj.channels.sms_channel import SmsChannel
from goonj.exception import SMSSettingNotFound, EmailSettingNotFound, ChannelsNotDefined, EmailChannelNotDefined, \
    SlackChannelNotDefined, SMSChannelNotDefined


class ChannelSettings(object):

    def __init__(self, channels, email_settings, sms_settings):
        """
        :param channels:

        channels={
        'email_channels':[{'to':'',from_add:'','name':''},   {'to':'',from_add:'','name':''}  ],
        'slack_channels':[{'webhook:'','name':''},{'webhook:'','name':''}]
        }s

        initializes channel_map given below and add settings to the channels
        channel_map=(
        email_channel=
                 {'email_channle_name1':email_channel_object1,
                  'email_channle_name2':email_channel_object2}
        sms_channel=
                 {'sms_channle_name1':sms_channel_object1,
                  'sms_channle_name2':smsl_channel_object2} )

        """
        if not channels:
            raise ChannelsNotDefined('No channels are defined ,define at least one cahnnel within \'channels\' or '
                                     'remove chennels settign completly if no channel is needed')

        if constants.CHANNEL_EMAIL in channels:
            self.email_channels = self.get_email_channels(
                channels[constants.CHANNEL_EMAIL])

            self.register_setting_to_email_channel(email_settings)

        if constants.CHANNEL_SLACK in channels:
            self.slack_channels = self.get_slack_channel(
                channels[constants.CHANNEL_SLACK])

        if constants.CHANNEL_SMS in channels:
            self.sms_channels = self.get_sms_channel(
                channels[constants.CHANNEL_SMS])

            self.register_setting_to_sms_channel(sms_settings)

    def register_setting_to_email_channel(self, email_settings):
        try:
            # register notification service if available
            EmailChannel.register_custom_email_notifcation_service(
                email_settings.notification_service)
            # register smtp configuration
            EmailChannel.register_smtp_server_config(
                email_settings.smtp_server_config)
        except AttributeError as e:
            raise EmailSettingNotFound('For email channels ,email_settings is not defined ,please define a custom '
                                       'service/smtp '
                                       'sever setting '
                                       'to '
                                       'handle email')

    def register_setting_to_sms_channel(self, sms_settings):
        try:
            SmsChannel.register_custom_sms_notifcation_service(
                sms_settings.notification_service)
        except AttributeError as e:
            raise SMSSettingNotFound('For Sms channels, sms_settings is not defined ,please define a custom '

                                     'service to handle sms')

    def get_email_channels(self, email_channels):
        if not email_channels:
            raise EmailChannelNotDefined('No Email Channel is defined for \'email_channels\' ,please add at least '
                                         'one email channel ,or if you dont need it remove \'email_channels\'')
        return {email_channel['name']: EmailChannel(**email_channel) for
                email_channel in email_channels}

    def get_slack_channel(self, slack_channels):
        if not slack_channels:
            raise SlackChannelNotDefined('No Slack Channel is defined for \'slack_channels\' ,please add at least '
                                         'one slack channel ,or if you dont need it remove \'slack_channels\'')
        return {slack_channel['name']: SlackChannel(**slack_channel) for
                slack_channel in slack_channels}

    def get_sms_channel(self, sms_channels):
        if not sms_channels:
            raise SMSChannelNotDefined('No SMS Channel is defined for \'sms_channels\' ,please add at least '
                                       'one slack channel ,or if you dont need it remove \'sms_channels\'')
        return {sms_channel['name']: SmsChannel(**sms_channel) for
                sms_channel in sms_channels}
