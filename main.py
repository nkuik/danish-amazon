import config.configuration as config

from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)
app.config.update(config.load_config())

@app.route("/")
async def root(request):
    return json({'hello': 'world'})

@app.route("/listening", methods=['POST'])
async def listening(request):
    return json({ "challenge": request.json['challenge'] })

def run():
    app.run(host="0.0.0.0")

if __name__ == '__main__':
    run()
