from goonj import core
from goonj.conf.constants import Sev
from goonj.core import get_smart_alert


def run_sample():
    goonj = core.Goonj(config_file_path='goonj.yaml')
    x = get_smart_alert('source_name1')
    x.send(Sev.HIGH, "dsgfds", "subjecr", error_id="1",
           tag_list=["tag1", "tag2"])
    print('wait maadi')


run_sample()
