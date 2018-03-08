import asyncore
from smtpd import SMTPServer


class EmlServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        pass


def run():
    EmlServer(('localhost', 1025), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
