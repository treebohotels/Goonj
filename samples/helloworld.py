import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/tmp/goonj.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

from goonj.core import Goonj, get_smart_alert
from goonj.conf.constants import Sev

#logger = logging.getLogger(__name__)

def run_sample():
    # initialize goonj
    Goonj(config_file_path='samples/goonj.yaml')

    x = get_smart_alert('source_name2', logger)

    x.info("TEST HIGH", sev=Sev.HIGH, subject="HIGH", error_id="1", error=None, tag_list=["tag1", "tag2"])
    x.info("TEST CRITICAL", sev=Sev.CRITICAL, subject="CRITICAL", error_id="1", error=None, tag_list=["tag11", "tag12"])
    x.info("only message ")

    print('wait maadi')


run_sample()
