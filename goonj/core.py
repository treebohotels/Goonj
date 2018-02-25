from goonj.conf.configuration import Configuration
from goonj.conf.constants import DEFAULT_CONFIG_FILE_PATH
from goonj.models.model_setup import init_database


class Goonj(object):

    def __init__(self, config_file_path=DEFAULT_CONFIG_FILE_PATH):

        self.config = Configuration(config_file=config_file_path)
        self.config.db = init_database(self.config.db_setting, self.config.app_id)






