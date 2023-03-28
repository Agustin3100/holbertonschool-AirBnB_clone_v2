#!/usr/bin/python3
"""is it a number?."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def display(name=None, strict_slashes=False):
    """Display Hello HBNB."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display2(name=None):
    """Display HBNB."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def txtreplace(text):
    """Display rotue and text."""
    text2 = text.replace('_', ' ')
    return 'C {}'.format(text2)


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def iscool(text):
    """Set a default value for text."""
    text2 = text.replace('_', ' ')
    return 'Python {}'.format(text2)


@app.route('/number/<int:n>', strict_slashes=False)
def isint(n):
    """Display n is a number only if it is an int."""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
