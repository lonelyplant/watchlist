from flask import render_template

from watchlist import app


@app.errorhandler(404)
def bad_request(e):
    return render_template('errors/404.html'), 404