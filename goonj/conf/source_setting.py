from goonj.channels.slack_channel import SlackChannel
from goonj.conf import constants
from goonj.entities import AlertSource, Recipient, HighSev, LowSev, MediumSev, CriticalSev


class SourceSettings(object):

    def __init__(self, sources):
        self.alert_sources = self.get_alert_sources(sources)

    def get_alert_sources(self, sources):
        return [self.initialize_alert_source(key, value) for key, value in sources.items()]

    def initialize_alert_source(self, key, value):
        default_channels_obj = self.get_channels(value['default_channels'])
        sev_obj = self.get_sev(value['sev'])
        return AlertSource(key, default_channels_obj, sev_obj)

    def get_channels(self, channels):
        channels_obj = []
        if 'slack_channel' in channels:
            recipients = self.get_recipients(channels['slack_channel'])
            channels_obj.append(SlackChannel(recipients))
        return channels_obj

    def get_sev(self, sev):
        sev_obj = []
        if 'low' in sev:
            channels_obj = self.get_channels(sev['low'])
            sev_obj.append(LowSev(channels_obj))

        if 'medium' in sev:
            channels_obj = self.get_channels(sev['medium'])
            sev_obj.append(MediumSev(channels_obj))

        if 'high' in sev:
            channels_obj = self.get_channels(sev['high'])
            sev_obj.append(HighSev(channels_obj))

        if 'critical' in sev:
            channels_obj = self.get_channels(sev['critical'])
            sev_obj.append(CriticalSev(channels_obj))

        return sev_obj

    def get_recipients(self, recipients):

        recipient_obj = set()
        for recipient in recipients:
            recipient_obj.add(Recipient(recipient['name'], recipient['type']))
        return recipient_obj
