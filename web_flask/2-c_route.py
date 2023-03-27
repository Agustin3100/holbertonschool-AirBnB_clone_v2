#!/usr/bin/python3
"""C is fun!."""
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
    text2 = text.replace('_', ' ')
    return f'C {text2}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
