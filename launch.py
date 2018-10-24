""" Flask launch utility """

import os
import argparse

parser = argparse.ArgumentParser()

# utility accepts the -d or --development flags
# to launch the flask server in development mode.

parser.add_argument(
    '-d', '--development',
    help='launch in development mode',
    action='store_true'
)
args = parser.parse_args()

if args.development:
    print('Launching Flask in development mode...')
    os.environ['FLASK_APP'] = 'launchwatch/app'
    os.environ['FLASK_ENV'] = 'development'
    os.system('flask run')
else:
    print('Launching Flask...')
    os.environ['FLASK_APP'] = 'launchwatch/app'
    os.system('flask run')