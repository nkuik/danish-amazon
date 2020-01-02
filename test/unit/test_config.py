import os
import mock
import unittest

import pytest

import config.configuration as config

class ConfigTests(unittest.TestCase):

    @mock.patch.dict(config.os.environ,
                     {'env': 'not prod'})
    def test_config_load_test(self):
        configuration = config.load_config()
        assert configuration.SLACK_SIGNING_SECRET == 'blah'
