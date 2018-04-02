class GoonjNotInitalized(Exception):
    pass


class SourceNotDefined(Exception):
    pass


class InvalidImplemnationOfNotifcationService(Exception):
    pass


class EmailChannelNotDefined(Exception):
    pass


class SlackChannelNotDefined(Exception):
    pass


class EmailChannelNameNotDefined(Exception):
    pass


class SlackChannelNameNotDefined(Exception):
    pass


class CustomNotificationModuleNotFound(Exception):
    pass


class ChannelsNotDefinedForSev(Exception):
    pass


class SmsChannelNameNotDefined(Exception):
    pass


class EmailChannelFromAddressNotDefined(Exception):
    pass


class EmailChannelToAddressNotDefined(Exception):
    pass


class SMSSettingNotFound(Exception):
    pass


class EmailSettingNotFound(Exception):
    pass
