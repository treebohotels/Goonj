from goonj.conf.configuration import Configuration
from goonj.conf.constants import DEFAULT_CONFIG_FILE_PATH
from goonj.exception import GoonjNotInitalized, SourceNotDefined
from goonj.smart_alert import SmartAlert

_sources = {}
goonj = None


def get_smart_alert(name, logger=None):
    """

    :param name: name of the source
    :return: if a source is not defined in config file initialize it with
             list of default_channels
    """
    if name in _sources:
        return _sources[name]

    if goonj is None:
        raise GoonjNotInitalized

    if goonj.config.sources.alert_sources[name] is None:
        raise SourceNotDefined

    _sources[name] = goonj.config.sources.alert_sources[name]

    return SmartAlert(name, _sources[name], logger)


class Goonj(object):
    __instance = None

    def __new__(cls, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Goonj, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, config_file_path=DEFAULT_CONFIG_FILE_PATH):
        global goonj
        if (self.__initialized):
            return
        self.__initialized = True
        self.config = Configuration(config_file=config_file_path)
        self.config.email = None

        goonj = self
