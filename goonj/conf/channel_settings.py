from goonj.channels import constants
from goonj.channels.email_channel import EmailChannel
from goonj.channels.slack_channel import SlackChannel
from goonj.channels.sms_channel import SmsChannel


class ChannelSettings(object):

    def __init__(self, channels, email_settings, sms_settings):
        """
        :param channels:

        channels={
        'email_channels':[{'to':'',from_add:'','name':''},   {'to':'',from_add:'','name':''}  ],
        'slack_channels':[{'webhook:'','name':''},{'webhook:'','name':''}]
        }

        initializes channel_map given below
        channel_map=(
        email_channel=
                 {'email_channle_name1':email_channel_object1,
                  'email_channle_name2':email_channel_object2}
        sms_channel=
                 {'sms_channle_name1':sms_channel_object1,
                  'sms_channle_name2':smsl_channel_object2} )

        """
        if constants.CHANNEL_EMAIL in channels:
            self.email_channels = self.get_email_channels(
                channels[constants.CHANNEL_EMAIL])

            # register notification service if available
            EmailChannel.register_custom_email_notifcation_service(
                email_settings.notification_service)

        if constants.CHANNEL_SLACK in channels:
            self.slack_channels = self.get_slack_channel(
                channels[constants.CHANNEL_SLACK])

        if constants.CHANNEL_SMS in channels:
            self.sms_channels = self.get_sms_channel(
                channels[constants.CHANNEL_SMS])

            SmsChannel.register_custom_sms_notifcation_service(
                sms_settings.notification_service)

    def get_email_channels(self, email_channels):
        return {email_channel['name']: EmailChannel(**email_channel) for
                email_channel in email_channels}

    def get_slack_channel(self, slack_channels):
        return {slack_channel['name']: SlackChannel(**slack_channel) for
                slack_channel in slack_channels}

    def get_sms_channel(self, sms_channels):
        return {sms_channel['name']: SmsChannel(**sms_channel) for
                sms_channel in sms_channels}
