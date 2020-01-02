import os


class Config(object):
    pass
    # Set these when settings are moved to parent directory
    # APP_DIR = os.path.abspath(os.path.dirname(__file__))
    # PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    def __call__(self):
        return self


class ProdConfig(Config):
    """Production configuration."""
    SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')

    ENV = 'prod'
    DEBUG = False



class DevConfig(Config):
    """Development configuration."""
    SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')
    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""
    SLACK_SIGNING_SECRET = 'blah'
    TESTING = True
    DEBUG = True


def load_config():
    if os.environ.get('env') == 'prod':
        return ProdConfig()
    if os.environ.get('env') == 'dev':
        return DevConfig()
    else:
        return TestConfig()
