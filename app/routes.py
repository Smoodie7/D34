from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return render_template("index.html")

@bp.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
