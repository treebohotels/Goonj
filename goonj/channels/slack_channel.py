
import logging
import json

from goonj.channels.base_channel import BaseChannel


class SlackChannel(BaseChannel):

    def send(self, severity, subject, body):

        logger = logging.getLogger(self.__class__.__name__)

        try:
            final_text = "{sev}: {sub}"
        #     url = settings.SLACK_CHANNEL_REVIEW_ALERT_URL
        #     payload = {"text": '`' + str(settings.ENVIRONMENT).upper() + "`: " + final_text}
        #     json_string = json.dumps(payload, default=lambda o: o.__dict__)
        #     headers = {'content-type': 'application/json'}
        #     requests.post(url, data=json_string, headers=headers)
        except Exception as e:
            logger.error("Error while alerting in slack(Ignoring) %s", e)
