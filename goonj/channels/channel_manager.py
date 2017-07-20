from goonj.channels import constants


class ChannelManager(object):

    channels = (constants.CHANNEL_LOGGER,
                constants.CHANNEL_EMAIL,
                constants.CHANNEL_SMS,
                constants.CHANNEL_SLACK)


