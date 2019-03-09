import os
import mock
import unittest

import config.configuration as config

class ConfigTests(unittest.TestCase):

    @mock.patch.dict(os.environ,
        {'SLACK_CLIENT_CONFIG': os.path.join(os.getcwd(), 'config/test.yml')})
    def test_config_load(self):
        configuration = config.load_config()
        assert configuration['slack']['command_token'] == 'test-token'

