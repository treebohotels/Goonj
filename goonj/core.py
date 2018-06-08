from goonj.conf.configuration import Configuration
from goonj.conf.constants import DEFAULT_CONFIG_FILE_PATH
from goonj.exception import GoonjNotInitalized, SourceNotDefined
from goonj.smart_alert import SmartAlert
from goonj.singleton import Singleton

_sources = {}
goonj = None


def get_smart_alert(name, logger=None):
    """

    :param name: name of the source
    :param logger: logger instance
    :return: source initailized with all the sev's and associated channels

    """
    if name in _sources:
        return _sources[name]

    if not goonj:
        raise GoonjNotInitalized

    if not goonj.config.sources.alert_sources[name]:
        raise SourceNotDefined('source {} is not defined in configuration file '.format(name))

    _sources[name] = SmartAlert(name, goonj.config.sources.alert_sources[name], logger)

    return _sources[name]


class Goonj(object, metaclass=Singleton):

    def __init__(self, config_file_path=DEFAULT_CONFIG_FILE_PATH):
        global goonj

        self.config = Configuration(config_file=config_file_path)

        """
        Goonj object content-
        goonj = {
                    'config': <goonj.conf.configuration.Configuration at 0x10e8aba58>
                    }
        config = {
                    'app_id': 'DefaultApp',
                    'import_paths': '.',
                    'config_file': 'samples/goonj.yaml',
                    'sms_settings': <goonj.conf.email_sms_settings.SmsSettings at 0x10e8d14e0>,
                    'email_settings': <goonj.conf.email_sms_settings.EmailSettings at 0x10e8d8ac8>,
                    'channels': <goonj.conf.channel_settings.ChannelSettings at 0x10e5f03c8>,
                    'sources': <goonj.conf.source_setting.SourceSettings at 0x10e8d1400>,
                    'db': None,
                    'email': None
                    }
        """

        goonj = self
