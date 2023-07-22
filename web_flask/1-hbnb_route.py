#!/usr/bin/python3
"""
    create a WSGI script with Flask to serve the application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """The root route to serve the application
        return: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    create a /hbnb route
    return HBNB!
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
