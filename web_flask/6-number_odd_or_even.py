from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    return render_template("5-number.html", num=escape(n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_route(n):
    return render_template("6-number_odd_or_even.html", num=escape(n))


if __name__ == "__main__":
    app.run(debug=True)
