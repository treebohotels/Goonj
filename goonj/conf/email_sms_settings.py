import importlib

from goonj.exception import CustomNotificationModuleNotFound


class EmailSettings(object):

    def __init__(self, email_settings):

        if 'smtp_server' in email_settings:
            self.host = email_settings['smtp_server']['host']
            self.port = email_settings['smtp_server']['port']
            self.username = email_settings['smtp_server']['username']
            self.password = email_settings['smtp_server']['password']

        if 'custom_notification_service' in email_settings:
            custom_notification_service = email_settings[
                'custom_notification_service']

            try:
                module_name, class_name = custom_notification_service.rsplit(
                    ".",
                    1)
                module = importlib.import_module(module_name)
                notification_service_class = getattr(module, class_name)
                notification_service = notification_service_class()
                self.notification_service = notification_service
            except Exception as e:
                raise CustomNotificationModuleNotFound('Custom Notifcation '
                                                       'service module not '
                                                       'found ,Please check '
                                                       'the package and '
                                                       'class name ,'
                                                       'for typos or any '
                                                       'other error')


class SmsSettings(object):

    def __init__(self, sms_settings):

        if 'custom_notification_service' in sms_settings:
            custom_notification_service = sms_settings[
                'custom_notification_service']

            try:
                module_name, class_name = custom_notification_service.rsplit(
                    ".",
                    1)
                module = importlib.import_module(module_name)
                notification_service_class = getattr(module, class_name)
                notification_service = notification_service_class()
                self.notification_service = notification_service
            except Exception as e:
                raise CustomNotificationModuleNotFound('Custom Notifcation '
                                                       'service module not '
                                                       'found ,Please check '
                                                       'the package and '
                                                       'class name ,'
                                                       'for typos or any '
                                                       'other error')
