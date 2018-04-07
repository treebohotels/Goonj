import logging

from goonj import core
from goonj.conf.constants import Sev
from goonj.core import get_smart_alert

logger = logging.getLogger(__name__)


def run_sample():
    # initilaize goonj
    core.Goonj(config_file_path='goonj.yaml')
    x = get_smart_alert('source_name1', logger)
    x.info(Sev.HIGH, "dsgfds", "subjecr", error_id="1", error=None,
           tag_list=["tag1", "tag2"])
    print('wait maadi')


run_sample()
