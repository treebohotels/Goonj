import email.utils
import smtplib
from email.mime.text import MIMEText

from goonj import core
from goonj.channels.base_channel import BaseChannel
from goonj.conf.constants import Sev


class EmailChannel(BaseChannel):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        dict of parameters required to initialze email channel,some field
        are optional like subject

        """
        self.from_add = kwargs['from_add']
        self.to = kwargs['to']
        self.name = kwargs['name']
        if 'subject' in kwargs:
            self.subject = kwargs['subject']

    def send(self, sev, message, subject=None, error_id=None,error=None,
             tag_list=None):

        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

        msg = MIMEText(message)
        msg['To'] = email.utils.formataddr(('Recipient',
                                            self.to))
        msg['From'] = email.utils.formataddr(('Author', self.from_add))
        msg['Subject'] = subject

        server = smtplib.SMTP(core.goonj.config.email.host,
                              core.goonj.config.email.port)
        server.set_debuglevel(True)  # show communication with the server

        try:
            server.sendmail(self.from_add, [self.to],
                            msg.as_string())
        finally:
            server.quit()

        pass
