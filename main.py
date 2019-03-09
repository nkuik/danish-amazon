from sanic import Sanic
from sanic.response import json

import config.configuration as config


app = Sanic(__name__)


@app.route('/')
async def root(request):
    return json({'hello': 'world'})

@app.route('/healthcheck')
async def root(request):
    def addition_works():
        if 1 + 1 == 2:
            return True, 'addition works'
        else:
            return False, 'the universe is broken'

    return json(addition_works())

@app.route('/listening', methods=['POST'])
async def listening(request):
    return json({ 'challenge': request.json['challenge'] })

@app.route('/depart', methods=['POST'])
async def depart(request):
    if ('token' not in request.form or
            not request.form['token'][0] == app.config['slack']['command_token']):
        return json(
            {'message': 'You shouldn\'t be here'},
            status = 401
        )

    return json({'token': request.form['token']})

def run():
    app.config.update(config.load_config())
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    run()
