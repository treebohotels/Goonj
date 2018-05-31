import email.utils
import smtplib
import threading
from email.mime.text import MIMEText

from goonj.channels.base_channel import BaseChannel
from goonj.conf.constants import Sev
from goonj.exception import InvalidImplemnationOfNotifcationService, \
    EmailChannelNameNotDefined, EmailChannelFromAddressNotDefined, \
    EmailChannelToAddressNotDefined


class BaseCustomEmailNotificationService(object):
    def send_email_notification(self, from_add, to, sev, message, subject,
                                error_id,
                                error,
                                tag_list):
        pass


class EmailChannel(BaseChannel):
    """
    Channel to send emails
    """

    notification_service = None
    smtp_server_config = None

    def __init__(self, **kwargs):
        """

        :param kwargs:
        dict of parameters required to initialize email channel,some field
            are optional like subject
        Initializing email channel using config

        """
        if 'name' not in kwargs:
            raise EmailChannelNameNotDefined(
                'Email channel name not defined ,\'name\' attribute is required')

        if 'from_add' not in kwargs:
            raise EmailChannelFromAddressNotDefined(
                'Email channel from_add not defined ,\'from_add\' attribute '
                'is '
                'required')

        if 'to' not in kwargs:
            raise EmailChannelToAddressNotDefined('Email Channel to address '
                                                  'is not define, \'to\' is '
                                                  'required field')

        self.from_add = kwargs['from_add']
        self.to = kwargs['to']
        self.name = kwargs['name']

        if 'subject' in kwargs:
            self.subject = kwargs['subject']

    @classmethod
    def register_custom_email_notifcation_service(cls,
                                                  notification_service):
        if not isinstance(notification_service,
                          BaseCustomEmailNotificationService):
            raise InvalidImplemnationOfNotifcationService('Custom '
                                                          'Notification '
                                                          'service should '
                                                          'implement '
                                                          'BaseCustomEmailNotificationService')

        cls.notification_service = notification_service

    @classmethod
    def register_smtp_server_config(cls, smtp_server_config):
        cls.smtp_server_config = smtp_server_config

    def send_message(self, sev, message, subject=None, error_id=None,
                     error=None,
                     tag_list=None):

        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

        if self.notification_service:
            self.notification_service.send_email_notification(self.from_add,
                                                              self.to,
                                                              sev,
                                                              message,
                                                              subject,
                                                              error_id,
                                                              error,
                                                              tag_list)

        elif self.smtp_server_config:

            msg = MIMEText(message)
            msg['To'] = email.utils.formataddr(('Recipient',
                                                self.to))
            msg['From'] = email.utils.formataddr(('Author', self.from_add))
            msg['Subject'] = subject

            server = smtplib.SMTP(self.smtp_server_config.host,
                                  self.smtp_server_config.port)

            try:

                server.sendmail(self.from_add, [self.to],
                                msg.as_string())
            except Exception as e:
                pass  # check how to handle logging in libraries
            finally:
                server.quit()

    # send email asynchronously
    def send(self, sev, message, subject=None, error_id=None,
             error=None,
             tag_list=None):
        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

        thread = threading.Thread(target=self.send_message, args=(sev, message,
                                                                  subject,
                                                                  error_id,
                                                                  error,
                                                                  tag_list),
                                  kwargs={})
        thread.start()
        # thread.join()
