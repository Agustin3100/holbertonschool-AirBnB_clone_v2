#!/usr/bin/python3
"""Python is cool!."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display(name=None):
    """Display Hello HBNB."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display2(name=None):
    """Display Hello HBNB."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def depending(text):
    """Display C and value of text."""
    url_defaults
    text2 = text.replace('_', ' ')
    return f'C {text2}'


@app.route('/python/',  defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def cool(text):
    """Print python followed by (default value)."""
    text2 = text.replace('_', ' ')
    return f'Python {text2}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
