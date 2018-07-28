import config.configuration as config

from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)

@app.route("/")
async def root(request):
    configuration = config.load_config()
    app.config.from_object(configuration)
    return json(app.config.items())

@app.route("/listening", methods=['POST'])
async def listening(request):
    return json({ "challenge": request.json['challenge'] })


def run():
    app.run(host="0.0.0.0")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
