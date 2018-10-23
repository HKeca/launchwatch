import os

from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.getenv('LAUNCHWATCH_SECRET', 'dev')
)


@app.route('/')
def root():
    return 'this is the root endpoint'