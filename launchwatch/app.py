""" Main LaunchWatch app module. """

import os

from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.getenv('LAUNCHWATCH_SECRET', 'dev')
)


@app.route('/')
def root():
    return jsonify({'endpoint': 'root'})