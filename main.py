import config.configuration as config

from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route("/")
async def root(request):
    app.config.from_object(config.load_config())
    return {'status': 'ok'}

@app.route("/listening", methods=['POST'])
async def listening(request):
    return json({ "challenge": request.json['challenge'] })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

