import logging
from time import sleep

from goonj import core
from goonj.conf.constants import Sev
from goonj.core import get_smart_alert

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/Users/sohitkumar/goonj.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


# logger = logging.getLogger(__name__)


def run_sample():
    # initilaize goonj
    core.Goonj(config_file_path='goonj.yaml')
    source_name1_alert = get_smart_alert('source_name1', logger)
    y = get_smart_alert('source_name1', logger)

    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("with rule engine ", sev=Sev.HIGH, subject="subject", error_id="1234", error=None,
                            tag_list=["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("dsgfds", Sev.HIGH, "subject", "1", None,
                            ["tag1", "tag2"])
    sleep(10)
    source_name1_alert.info("only message ", sev=Sev.HIGH, subject="asd")
    sleep(10)
    source_name1_alert.info("no sev")

    print('wait maadi')


def run_sample1():
    # initilaize goonj
    core.Goonj(config_file_path='goonj.yaml')
    source_name1_alert = get_smart_alert('source_name1', logger)
    source_name1_alert.info("dsgfds", sev=Sev.HIGH, subject="subject", error_id="1", error=None,
                            tag_list=["tag1", "tag2"])
    source_name1_alert.info("dsgfds", Sev.HIGH, "subject", "1", None,
                            ["tag1", "tag2"])
    source_name1_alert.info("only message ", sev=Sev.HIGH)
    source_name1_alert.info("no sev")

    print('wait maadi')


run_sample()
