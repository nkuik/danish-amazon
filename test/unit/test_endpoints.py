import os
import mock
import json
import unittest
import pkg_resources

import config.configuration as config

from main import app


def open_data_file(filename, read_mode='r'):
    path = pkg_resources.resource_filename('test', 'data')
    filepath = os.path.join(path, filename)
    with open(filepath, read_mode) as data_file:
        content = data_file.read()
    return content


class ConfigTests(unittest.TestCase):

    @mock.patch.dict(os.environ,
        {'DANISH_AMAZON_CONFIG': f"{os.getcwd()}/config/test.yml"})
    def test_oath_authentication(self):
        data = json.loads(open_data_file('oauth.json'))
        request, response = app.test_client.post('/listening', data=json.dumps(data))
        assert response.status == 200
        assert response.json == {'challenge': '3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P'}

    def test_wrong_authorization_request(self):
        pass