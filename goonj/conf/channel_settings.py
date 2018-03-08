from goonj.channels import constants
from goonj.channels.email_channel import EmailChannel
from goonj.channels.slack_channel import SlackChannel


class ChannelSettings(object):

    def __init__(self, channels):
        """

        :param channels: given map of 'type of channels','list of  channels
                         metadata' initializes
                         {'channel_type',{'name','channel_object'}
        """
        if constants.CHANNEL_EMAIL in channels:
            self.email_channels = self.get_email_channels(
                channels[constants.CHANNEL_EMAIL])
        if constants.CHANNEL_SLACK in channels:
            self.slack_channels = self.get_slack_channel(
                channels[constants.CHANNEL_SLACK])

    def get_email_channels(self, email_channels):
        return {email_channel['name']: EmailChannel(**email_channel) for
                email_channel in email_channels}

    def get_slack_channel(self, slack_channels):
        return {slack_channel['name']: SlackChannel(**slack_channel) for
                slack_channel in slack_channels}
