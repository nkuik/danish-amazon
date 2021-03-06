from sanic import Sanic
from sanic.response import json
from sanic.log import logger

import utilities as utilities
import config.configuration as config

app = Sanic(__name__)


@app.route('/')
async def root(request):
    return json({'hello': 'world'})


@app.route('/healthz')
async def healthz(request):
    logger.info('Healthz request was made')
    def addition_works():
        if 1 + 1 == 2:
            return True
        else:
            return False

    return json(addition_works())


@app.route('/depart', methods=['POST'])
async def depart(request):
    if (request.headers.get('X-Slack-Request-Timestamp') is not None
        and utilities.hash_matches(request.headers['X-Slack-Request-Timestamp'], app.config['SLACK_SIGNING_SECRET'])):
        return json({'message': 'good to see you'},
                    status = 200)
    else:
        return json(
            {'message': 'You shouldn\'t be here'},
            status = 401
        )


def run():
    app.config.from_object(config.load_config())
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    run()
