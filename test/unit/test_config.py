import os
import mock
import unittest

import pytest

from config import configuration

class ConfigTests(unittest.TestCase):

    @mock.patch.dict(configuration.os.environ,
                     {'env': 'not prod'})
    def test_config_load_test(self):
        configuration = configuration.load_config()
        assert configuration.SLACK_SIGNING_SECRET == 'blah'

    @mock.patch.dict(os.environ,
                     {'env': 'dev', 'SLACK_SIGNING_SECRET': 'dev_secret'})
    def test_dev_config(self):
        dev_config = configuration.DevConfig()
        assert dev_config.SLACK_SIGNING_SECRET == 'dev_secret'


    # @mock.patch.dict(configuration.os.environ,
    #                  {'env': 'dev', 'SLACK_SIGNING_SECRET': 'dev_secret'})
    @mock.patch.dict(os.environ, {'env': 'dev', 'SLACK_SIGNING_SECRET': 'dev_secret'})
    def test_config_load_dev(self):
        configuration = configuration.load_config()
        assert configuration.SLACK_SIGNING_SECRET == 'dev_secret'


    @mock.patch.dict(configuration.os.environ, {'env': 'prod'})
    @mock.patch.dict(configuration.os.environ,
                     {'SLACK_SIGNING_SECRET': 'prod_secret'})
    def test_config_load_prod(self):
        configuration = configuration.load_config()
        assert configuration.SLACK_SIGNING_SECRET == 'prod_secret'
