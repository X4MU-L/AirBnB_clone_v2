#!/usr/bin/python3
"""
    create a WSGI script with Flask to serve the application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def get_states():
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_down(res_or_except=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
