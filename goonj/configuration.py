# -*- coding: utf-8 -*-

import logging
import traceback

import constants
import yaml


class Configuration(object):
    """
    used to configure the service
    """

    def __init__(self, **kwargs):
        """
        :param test: the test config
        :param config_file: the path to store configuration
        """

        # first initialize everything with defaults
        self.load_with_defaults()

        # then check if config file is there if yes then load from it
        if 'config_file' in kwargs:
            self.config_file = kwargs['config_file']

        self.load_from_file(self.config_file)

        # now load any run time config change done
        self.set_config(**kwargs)

    def load_with_defaults(self):
        self.config_file = constants.DEFAULT_CONFIG_FILE

    def set_config(self, **kwargs):
        """
        set config values
        :param kwargs: contains the dict with all key values
        :return: 
        """
        if 'test' in kwargs:
            self.test = kwargs['test']

        if 'config_file' in kwargs:
            self.config_file = kwargs['config_file']

    def load_from_file(self, file_path):
        logger = logging.getLogger(self.__class__.__name__)
        try:
            with open(file_path, 'r') as stream:
                loaded_config = yaml.load(stream)
                self.set_config(**loaded_config)
        except Exception as e:
            traceback.print_exc()
            logger.error("Unable to load config file: {0} with exception {1}".format(str(file_path), e.message))
            self.load_with_defaults()
            self.dump_to_file(file_path)

    def dump_to_file(self, file_path):
        logger = logging.getLogger(self.__class__.__name__)
        conf_dict = {
            "test": self.test
        }

        try:
            config_file = open(file_path, "w")
            yaml.safe_dump(conf_dict, config_file, default_flow_style=False)
            config_file.close()
        except Exception as e:
            traceback.print_exc()
            logger.error("Unable to dump config file: {0} with exception {1}".format(str(file_path), e.message))
