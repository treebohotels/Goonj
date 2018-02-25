import abc

class BaseChannel(object):
    """
    Base class for all alerting channels
    """

    def __init__(self, recipient_list=set()):
        self._recipients = recipient_list

    def recipient_list(self):
        """
        get the recipient list
        :return: the recipient list
        """
        return self._recipients

    def add_recipient(self, recipient):
        """
        Adds a recipient to the list
        :param recipient: 
        :return: 
        """
        self._recipients.add(recipient)

    def remove_recipient(self, recipient):
        """
        remove a recipient from the list
        :param recipient: 
        :return: 
        """
        self._recipients.remove(recipient)

    @abc.abstractmethod
    def send(self, severity, subject, body):
        """
        Abstract function for message sending
        :param severity: 
        :param subject: 
        :param body: 
        :return: 
        """
        pass

    @abc.abstractmethod
    def validate_recipient(self, recipient):
        """
        Abstract function to validate the recipient
        :param recipient: the recipient to be validated
        :return: true/false
        """
        pass
