# -*- coding: utf-8 -*-

import logging
import traceback

import yaml

from goonj.conf import constants
from goonj.conf.channel_settings import ChannelSettings
from goonj.conf.email_sms_settings import EmailSettings, SmsSettings
from goonj.conf.source_setting import SourceSettings
from goonj.utils import update_import_paths


class Configuration(object):
    """
    used to configure the service
    """

    def __init__(self, **kwargs):
        """
        :param app_name: the application specific unique name.
        :param db_type: what is the database type
        :param db_name: the name of the database
        :param db_user: user information of the database
        :param db_password: the password of the database
        :param db_node: the node of the database
        :param config_file: the path of the config file
        :param import_paths: the import path location
        """

        # first initialize everything with defaults
        self.load_with_defaults()

        # then check if config file is there if yes then load from it
        if 'config_file' in kwargs:
            self.config_file = kwargs['config_file']

        self.load_from_file(self.config_file)

        # now load any run time config change done
        self.set_config(**kwargs)

        self.db = None

    def load_with_defaults(self):
        self.app_id = constants.DEFAULT_APP_ID
        self.import_paths = constants.DEFAULT_IMPORT_PATHS
        self.config_file = constants.DEFAULT_CONFIG_FILE_PATH
        self.sms_settings = None
        self.email_settings = None
        self.channels = None

        update_import_paths(self.import_paths)

    def set_config(self, **kwargs):
        """
        set config values
        :param kwargs: contains the dict read from config file ,with all key
        values
        :return:
        """

        if 'app_id' in kwargs:
            self.app_id = kwargs['app_id']

        if 'import_paths' in kwargs:
            self.import_paths = kwargs['import_paths']
            update_import_paths(self.import_paths)

        if 'config_file' in kwargs:
            self.config_file = kwargs['config_file']

        if 'email_settings' in kwargs:
            self.email_settings = EmailSettings(kwargs['email_settings'])

        if 'sms_settings' in kwargs:
            self.sms_settings = SmsSettings(kwargs['sms_settings'])

        if 'channels' in kwargs:
            self.channels = ChannelSettings(kwargs['channels'],
                                            self.email_settings,
                                            self.sms_settings)

        if 'sources' in kwargs:
            self.sources = SourceSettings(kwargs['sources'], self.channels)

    def load_from_file(self, file_path):
        logger = logging.getLogger(self.__class__.__name__)
        try:
            with open(file_path, 'r') as stream:
                loaded_config = yaml.load(stream)
                self.set_config(**loaded_config)
        except Exception as e:
            traceback.print_exc()
            logger.error(
                "Unable to load config file: {0} with exception {1}".format(
                    str(file_path), e))
            raise e
