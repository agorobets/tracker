from flask import Flask
from flask import Response
from flask import request
import base64
import os
import json
from datetime import datetime

PIXEL_DATA = base64.b64decode("R0lGODlhAQABAIAAAP8AAP8AACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)


@app.route("/logo.gif")
def index():
    path = f'{BASE_DIR}/requests/{request.remote_addr}'
    if not os.path.exists(path):
        os.mkdir(path, mode=0o777)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = f'{path}/{timestamp}.json'
    with open(filepath, 'w+') as f:
        json.dump(dict(
            referrer=request.referrer,
            date=request.date,
            remote_addr=request.remote_addr,
            headers=dict(request.headers),
        ), f)

    return Response(PIXEL_DATA, mimetype="image/gif")

