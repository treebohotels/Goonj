import abc

from goonj.async_process import AsyncProcess
from goonj.conf.constants import Sev


class BaseChannel(object):
    """
    Base class for all alerting channels
    """

    @abc.abstractmethod
    def _send_message(self, sev, message, subject=None, error_id=None, error=None, tag_list=None):
        raise NotImplemented

    def send(self, sev, message, subject=None, error_id=None, error=None, tag_list=None):
        """

        :param sev:
        :param message:
        :param subject:
        :param error_id:
        :param error:
        :param tag_list:
        :return:
        """

        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

        AsyncProcess.async_processor(self._send_message,
                                     args=(sev, message, subject, error_id, error, tag_list),
                                     kwargs={})
