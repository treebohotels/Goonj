
import abc


class BaseChannel(object):
    """
    Base class for all alerting channels
    """

    @abc.abstractmethod
    def send(self, category, message):

        pass
