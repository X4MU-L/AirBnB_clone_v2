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
    """
    gets a list of all states in the storage and
    return html page to render page
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def get_cities_state():
    """get cities in each state"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tear_down(res_or_except=None):
    """Tear down app context"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
