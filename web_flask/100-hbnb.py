#!/usr/bin/python3
"""
    create a WSGI script with Flask to serve the application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def render_page():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def tear_down(res_or_except=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
