import os
import mock
import json
import unittest
import pkg_resources

from main import app


def open_data_file(filename, read_mode='r'):
    path = pkg_resources.resource_filename('test', 'data')
    filepath = os.path.join(path, filename)
    with open(filepath, read_mode) as data_file:
        content = data_file.read()
    return content


class ConfigTests(unittest.TestCase):

    @mock.patch('main.config.load_config', return_value={'this':'that'})
    def test_home_page(self, __):
        request, response = app.test_client.get('/')
        assert response.status == 200
        assert response.json == {'hello': 'world'}

    @mock.patch('main.config.load_config', return_value={'this':'that'})
    def test_health_endpoint(self, mock_app_config):
        request, response = app.test_client.get('/healthcheck')
        assert response.status == 200
        assert response.json == [True, 'addition works']

    @mock.patch('main.config.load_config', return_value={'this':'that'})
    def test_oath_authentication(self, mock_app_config):
        data = json.loads(open_data_file('oauth.json'))
        request, response = app.test_client.post('/listening', data=json.dumps(data))
        assert response.status == 200
        assert response.json == {
            'challenge': data['challenge']
        }