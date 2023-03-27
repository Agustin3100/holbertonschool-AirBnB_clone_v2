#!/usr/bin/python3
"""Display HBNB."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def display(name=None, strict_slashes=False):
    """Display Hello HBNB."""
    return 'Hello HBNNB!'


@app.route('/hbnb')
def diplsay2(name=None, strict_slashes=False):
    """Display HBNB."""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
