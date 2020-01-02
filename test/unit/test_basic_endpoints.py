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

command_response = "channel_id=CFPRYTN3D&token=test-token&channel_name=logistics&command=/depart&response_url=https://hooks.slack.com/commands/T90FV7BCN/535414414022/ZJIhUlIHhTUXkY5js3cKC35V&team_domain=getyourshittogethernk&team_id=T90FV7BCN&trigger_id=535055286759.306539249430.4d15d5e01b59b5e562b8dc560216235d&user_id=U8Z0Z2C3S&user_name=nathan.kuik"


class ConfigTests(unittest.TestCase):

    def test_home_page(self):
        request, response = app.test_client.get('/')

        assert response.status == 200
        assert response.json == {'hello': 'world'}


    def test_health_endpoint(self):
        request, response = app.test_client.get('/healthcheck')

        assert response.status == 200
        assert response.json == [True, 'addition works']


    def test_matching_signing_hash_sends_200(self):
        headers = {'X-Slack-Request-Timestamp': '01/01/2020'}
        app.config.from_object(config.load_config())
        _, response = app.test_client.post('/depart',
                                           data=json.dumps({}),
                                           headers=headers)

        assert response.status == 200


    def test_non_matching_hash_sends_401(self):
        headers = {'X-Slack-Request-Timestamp': '01/01/2020'}
        app.config.from_object(config.load_config())
        app.config['SLACK_SIGNING_SECRET'] = 'wrong!'
        _, response = app.test_client.post('/depart',
                                           data=json.dumps({}),
                                           headers=headers)
        assert response.status == 401


    def test_post_without_timestamp(self):
        headers = {'empty': 'not here'}
        app.config.from_object(config.load_config())
        app.config['SLACK_SIGNING_SECRET'] = 'wrong!'
        _, response = app.test_client.post('/depart',
                                           data=json.dumps({}),
                                           headers=headers)
        assert response.status == 401
