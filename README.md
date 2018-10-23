# LaunchWatch [![CircleCI](https://circleci.com/gh/elliott-maguire/launchwatch.svg?style=svg&circle-token=2f58c0ef74352215db889dcefbbc54d0f52b7a1e)](https://circleci.com/gh/elliott-maguire/launchwatch)

*The smartest Rocket League API around.*

***NOTICE:*** This project is for **fun** and **education**.
It is by no means something to get in a fuss over. If you're here and you are experienced, we ask that you refrain from judging or belittling those who may not have as much experience. And to those of you who are new, please use this as an opportunity to learn and grow; expect constructive criticism, and always keep a growth mindset.

### So, what is *LaunchWatch*?
*LaunchWatch* is an API written in [Python 3.7](https://www.python.org/downloads/release/python-370/), and built with the [Flask](http://flask.pocoo.org/) web framework. The coolest (planned) part of LaunchWatch is its `StreamRead` tech that (God willing) allows it to actively read live time and score data from any given Rocket League stream online. However, the general purpose is to deliver the most up-to-date RLCS data, including teams, standings, past, active, and planned matches, and much more.

### How can I help?
You can do **pretty much anything.** As long as it's something that contributes to the project in whole, whether it be docs or code, it is appreciated and we invite you to contribute.

## Project Guidelines

### Collaboration
As stated before, this is a project targeted towards **collaboration**, **education**, and a **good time coding cool stuff**. That said, the structure of the project will parallel that of a more serious project. Tests and builds will be processed via [CircleCI](https://circleci.com/product/), Issues will be templated and automatically tracked in Projects, every scrap of code will be reviewed before it is merged with `master`, and all collaborators will be verified by maintainers before they are permitted to start their collaboration. 

### Styling
This project will abide by [PEP 8 standards](https://www.python.org/dev/peps/pep-0008/). Please do your best to keep your code continuous with the rest. Do your best to write well - even if you're a beginner and it takes a little more time, always get in the habit of writing good code.

### Branching/Versioning
Semantic versioning and clear branch naming is **very important.** If you create a branch or pull request with a mess of a name, it will be rejected. Your branches should follow this format:

- Version Name (should only be done by admins): `v1.3.2`
- Issue Name (should be done by asignee): `issue-12`
- Change Name (should hopefully be done by asignee): `setup-auth`

## Project Features/Goals with *Trendy Startup Names*
1. **Readr** - a NumPy-based system that reads image data from livestreams for game data (teams, score, time, etc). This is a reach goal but would be REALLY REALLY COOL if we got it working.
2. **Clctr** - an advanced set of bots and utilities that crawls the web for the newest game data, always pulling the best of the best into the database. This will be much easier than StreamRead, but will still be a rad feature.
3. **Guesr** - a simple AI (series of conditionals) that makes predictions on game outcomes. (`if team_1.wins > team_2.wins: winner = team_1`)
4. **ANY OTHER IDEAS!** - the cool thing here is that we can just build whatever would be cool and productive to learn about, so throw feature suggestions into the Issues!

## Project Setup
#### Necessary for Development:
1. [Python 3.7](https://www.python.org/downloads/release/python-370/)
2. [Flask](http://flask.pocoo.org/)
3. [PostgreSQL](https://www.postgresql.org/download/)
4. [pipenv 2018.10.13](https://pipenv.readthedocs.io/en/latest/)
5. [Project Dependencies](https://github.com/elliott-maguire/launchwatch/blob/master/Pipfile)

If you don't know anything about the above technologies, please refer to their respective documentation.

### Get Started
1. Clone the repo (duh).
2. Run `pipenv --python 3.7` to create a virtualenv for you local project.
3. Run `pipenv update` to update and lock all dependencies.
4. Run `python launch.py` to run the server.

Useful commands to know:
- `python launch.py` runs a utility module that sets up and runs the server. Use the `-d` or `--development` flags to run a development server.