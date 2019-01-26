import os
import yaml


def load_config():
    with open(os.environ['SLACK_CLIENT_CONFIG'], 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return config
