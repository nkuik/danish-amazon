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

command_response = "channel_id=CFPRYTN3D&token=f5CJDWrbEGAkKeyqODyev6T9&channel_name=logistics&command=/depart&response_url=https://hooks.slack.com/commands/T90FV7BCN/535414414022/ZJIhUlIHhTUXkY5js3cKC35V&team_domain=getyourshittogethernk&team_id=T90FV7BCN&trigger_id=535055286759.306539249430.4d15d5e01b59b5e562b8dc560216235d&user_id=U8Z0Z2C3S&user_name=nathan.kuik"


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

    @mock.patch.dict(os.environ,
        {'SLACK_CLIENT_CONFIG': os.path.join(os.getcwd(), 'config/config.yml')})
    def test_matching_command_token_sends_200(self):
        configuration = config.load_config()
        headers = {"content-type": "application/x-www-form-urlencoded"}
        request, response = app.test_client.post('/depart',
            data=command_response, headers=headers)

        assert response.status == 200


    @mock.patch.dict(os.environ,
        {'SLACK_CLIENT_CONFIG': os.path.join(os.getcwd(), 'config/config.yml')})
    def test_checks_for_token(self):
        configuration = config.load_config()
        headers = {"content-type": "application/x-www-form-urlencoded"}
        request, response = app.test_client.post('/depart',
            data=command_response, headers=headers)
