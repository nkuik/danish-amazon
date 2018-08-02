from sanic import Sanic
from sanic.response import json

import config.configuration as config


app = Sanic(__name__)


@app.route("/")
async def root(request):
    return json({'hello': 'world'})

@app.route("/healthcheck")
async def root(request):

    def addition_works():
        if 1 + 1 == 2:
            return True, "addition works"
        else:
            return False, "the universe is broken"

    return json(addition_works())

@app.route("/listening", methods=['POST'])
async def listening(request):
    return json({ "challenge": request.json['challenge'] })

def run():
    app.config.update(config.load_config())
    app.run(host="0.0.0.0")

if __name__ == '__main__':
    run()
