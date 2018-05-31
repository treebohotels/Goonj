import threading

from goonj.channels.base_channel import BaseChannel
from goonj.conf.constants import Sev
from goonj.exception import SmsChannelNameNotDefined, \
    InvalidImplemnationOfNotifcationService


class BaseCustomSmsNotificationService(object):
    def send_sms_notification(self, phone_numbers, sev, message, subject,
                              error_id,
                              error,
                              tag_list):
        pass


class SmsChannel(BaseChannel):
    notification_service = None

    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise SmsChannelNameNotDefined(
                'Sms channel name not defined ,\'name\' attribute is required')

        self.phone_numbers = kwargs['phone_numbers']

    @classmethod
    def register_custom_sms_notifcation_service(self,
                                                notification_service):
        if not isinstance(notification_service,
                          BaseCustomSmsNotificationService):
            raise InvalidImplemnationOfNotifcationService('Custom '
                                                          'Notification '
                                                          'service should '
                                                          'implement '
                                                          'BaseCustomSmsNotificationService')

        self.notification_service = notification_service

    def send_message(self, sev, message, subject=None, error_id=None,
                     error=None,
                     tag_list=None):

        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

        if self.notification_service is None:
            return  # log here that no notifcation service is registerd

        self.notification_service.send_sms_notification(self.phone_numbers,
                                                        sev,
                                                        message,
                                                        subject,
                                                        error_id,
                                                        error,
                                                        tag_list)

    # send sms asynchronously
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
