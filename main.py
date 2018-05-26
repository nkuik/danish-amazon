import config.configuration as config

CONFIG = None

def run():
    running = True
    while running:
        CONFIG = config.load_config()
