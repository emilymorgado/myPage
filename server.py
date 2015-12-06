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
    """Homepage welcomes and links to further information"""

    return render_template("home.html")


@app.route('/python')
def python():
    """Shows examples of my use of Python"""

    return render_template("python.html")


@app.route('/javascript')
def javascript():
    """Shows examples of my use of JS, jQuery, and AJAX"""

    return render_template("js.html")

@app.route('/sql')
def sql():
    """Shows examples of my use of SQLite and SQLAlchemy"""

    return render_template("sql.html")


@app.route('/framework')
def flask():
    """Shows examples of my use of Flask and Jinja"""

    return render_template("flask.html")


@app.route('/api')
def google_maps():
    """Shows examples of my use of Google Maps API"""

    return render_template("api.html")


@app.route('/html')
def html():
    """Shows examples of my use of html"""

    return render_template("html.html")


@app.route('/css')
def css():
    """Shows examples of my use of html"""

    return render_template("css.html")


@app.route('/front-end')
def front_end():
    """Shows examples of my use of html"""

    return render_template("boot.html") 


@app.route('/extra')
def front_end():
    """Shows examples of my use of html"""

    return render_template("extra.html")        


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()