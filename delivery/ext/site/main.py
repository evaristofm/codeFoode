from flask import Blueprint, render_template, redirect, url_for
from delivery.ext.auth.forms import UserForm

from delivery.ext.db import db
from delivery.ext.auth.models import User


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")

@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("site.index"))

    return render_template("userform.html", form=form)


