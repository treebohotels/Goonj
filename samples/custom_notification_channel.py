from goonj.channels.email_channel import BaseCustomEmailNotificationService
from goonj.channels.sms_channel import BaseCustomSmsNotificationService


class CustomNotificationService(BaseCustomEmailNotificationService,
                                BaseCustomSmsNotificationService):

    def send_email_notification(self, from_add, to, sev, message, subject,
                                error_id,
                                error,
                                tag_list):
        print('sending  email from custom service')

    def send_sms_notification(self, phone_numbers, sev, message, subject,
                              error_id,
                              error,
                              tag_list):
        print('sending sms notification')
