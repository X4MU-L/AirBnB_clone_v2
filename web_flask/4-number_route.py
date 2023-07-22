#!/usr/bin/python3
"""
    create a WSGI script with Flask to serve the application
"""
from flask import Flask
from markupsafe import escape

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


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    create a dynamic c route
    path: /c/<strings delimited by '-'>
    text: any
    return: C <text delimeted by space if text contains '-'>
    """
    text = escape(text).replace('_', ' ')
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is_cool"):
    """
    create a dynamic python route
    path: /python/<strings delimited by '-'>
    text: any
    return: Python <text delimeted by space if text contains '-'>
    """
    text = escape(text).replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    create a dynamic route for number with an int contraint
    return: <n> is a number
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(debug=True)
