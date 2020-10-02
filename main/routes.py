import os
import secrets
from flask import render_template, url_for, flash, redirect
from main import app, db
from main.forms import LoginForm, PredictForm, ImageUpload
from random import randint

from main.models import Image

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/status")
def status():
    return render_template("status.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login success for {form.username.data} with password length of: {len(form.password.data)}!",
            "success",
        )
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = PredictForm()
    value = randint(2000, 5000)
    if form.validate_on_submit():
        flash(f"Prediction: {value}", "success")
        return redirect(url_for("home"))
    return render_template("predict.html", title="Predict", form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/image", methods=["GET", "POST"])
def image():
    form = ImageUpload()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        flash('Your image has been updated!', 'success')
        return redirect(url_for('image'))
    image_file = url_for('static', filename='profile_pics/*.png')
    return render_template("image.html", title="Image",image_file=image_file, form=form)

