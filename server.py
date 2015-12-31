"""Class Finder Flask Routes"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


# This is how Flask knows what module to scan for things like routes
app = Flask(__name__)


app.secret_key = "tamandua"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def welcome():
    """Homepage contains modal windows with information. This is a single page site."""

    return render_template("home.html")



if __name__ == "__main__":

    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()