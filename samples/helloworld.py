import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/Users/sohitkumar/goonj.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

from goonj import core
from goonj.conf.constants import Sev
from goonj.core import get_smart_alert

#logger = logging.getLogger(__name__)


def run_sample():
    # initilaize goonj
    core.Goonj(config_file_path='goonj.yaml')
    x = get_smart_alert('source_name1', logger)
    x.info( "dsgfds", sev=Sev.HIGH, subject="subjecr", error_id="1", error=None,
           tag_list=["tag1", "tag2"])
    x.info("only message")


    print('wait maadi')


run_sample()
