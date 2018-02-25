# self.send(self._default_source, severity, subject, message, tag_list=tag_list, channel_list=channel_list)
class MessageHandler(object):

    def send_message(self, channel_list, severity, subject, description, error_id, tag_list):
        for channel in channel_list:
            channel.send(severity, subject, description, error_id, tag_list)

    def save_message(self):
        pass
