import abc


class BaseChannel(object):
    """
    Base class for all alerting channels
    """

    @abc.abstractmethod
    def send(self, sev, message, subject, error_id, error, tag_list):
        """

        :param sev:
        :param description:
        :param subject:
        :param error_id:
        :param error:
        :param tag_list:
        :return:
        """

    pass
