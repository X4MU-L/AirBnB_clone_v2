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


if __name__ == "__main__":
    app.run()
