from flask import Flask, g
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    text = escape(text).replace('_', ' ')
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is_cool"):
    text = escape(text).replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(debug=True)
