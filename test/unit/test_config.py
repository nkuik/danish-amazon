import os
import unittest

import config.configuration as config

class ConfigTests(unittest.TestCase):

    def test_config_load(self):
        if os.environ['DANISH_AMAZON_ENV'] == 'dev':
            os.environ['DANISH_AMAZON_CONFIG'] = f"{os.getcwd()}/config/test.yml"
        configuration = config.load_config()
        assert configuration['twilio']['api-key'] == 'twilio-api-key'

