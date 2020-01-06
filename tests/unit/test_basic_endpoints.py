import os
import mock
import json
import unittest
import pkg_resources

import config.configuration as config

from main import app


class ConfigTests(unittest.TestCase):

    def test_home_page(self):
        request, response = app.test_client.get('/')

        assert response.status == 200
        assert response.json == {'hello': 'world'}


    def test_health_endpoint(self):
        request, response = app.test_client.get('/healthz')

        assert response.status == 200
        assert response.json == True


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
