from goonj.entities import ErrorConfig


class ErrorConfigSetting(object):

    def __init__(self, error_code_settings):
        self.error_code_config = {}
        if error_code_settings and len(error_code_settings) > 0:
            for error_code_setting in error_code_settings:
                self.error_code_config[str(error_code_setting['error_code'])] = ErrorConfig(str(error_code_setting[
                                                                                           'error_code']),
                                                                                       error_code_setting['threshold'])


