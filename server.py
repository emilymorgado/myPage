"""Emily's myPage Flask Routes"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


# This is how Flask knows what module to scan for things like routes
app = Flask(__name__)


app.secret_key = "tamandua!"
# app.secret_key = FLASK_SECRET_KEY
# app.config.from_secrets('secret_key')
# SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")

app.jinja_env.undefined = StrictUndefined


@app.route('emilymorgado.com/')
def welcome():
    """Contains modal windows with information. This is a single page site."""

    return render_template("home.html")



if __name__ == "__main__":

    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()