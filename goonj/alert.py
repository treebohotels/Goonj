from goonj.channels.channel_manager import ChannelManager

def send(source, severity, subject, message, tag_list=None, channel_list=None):

    if not channel_list:
        channel_list = ChannelManager.channels



class SmartAlert(object):

    def __init__(self, source, channel_list=None):
        self._default_source = source
        self._default_channel_list = channel_list

    def send(self, severity, subject, message, tag_list=None, channel_list=None):
        if not channel_list:
            channel_list = self._default_channel_list
        self.send(self._default_source, severity, subject, message, tag_list=tag_list, channel_list=channel_list)


        # save the messages in db




