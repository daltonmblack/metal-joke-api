# metal-joke-api
API that serves metal music jokes

## Initial Setup

* Validate that Python 3.8 is installed (e.g., `python -V`)
  * If you have both Python 2 and Python 3 installed, you will need to use `python3` in place of `python` in the commands below
  * If Python 3.8 isn't installed anywhere on your system, one option is to install it using `pyenv`: https://realpython.com/intro-to-pyenv/
* Install `poetry` which is used to install the packages for this project: https://python-poetry.org/docs/
* Install the packages required for this project
```
poetry install
```

## Running Metal Joke API

```
poetry run start
```

## Instructions for Maintainers

### Deploying to Deta

```
deta deploy metaljokeapi
```

### Publishing to PyPi

```
poetry build
poetry publish
```
