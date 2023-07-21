from flask import Flask
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
    text = ' '.join(escape(text).split('_'))
    return f"C {text}"


if __name__ == "__main__":
    app.run(debug=True)
