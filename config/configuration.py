import os
import yaml


def load_config():
    with open(os.environ['DANISH_AMAZON_CONFIG'], 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return config
