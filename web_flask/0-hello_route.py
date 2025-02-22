#!/usr/bin/python3
"""
Task 0: script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello(strict_slashes=False):
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
