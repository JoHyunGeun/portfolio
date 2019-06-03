import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from . import app, db, bcrypt
from .forms import ClassificationForm
from .models import User
from sqlalchemy import desc
from .classifier import Classifier


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/finger_pics', picture_fn)

    output_size = (224, 224)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/", methods=['POST', 'GET'])
@app.route("/classification", methods=['POST', 'GET'])
def classification():
    form = ClassificationForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        user = User(username=form.username.data, phone_number=form.phone_number.data, image_file=picture_file)
        db.session.add(user)
        db.session.commit()
        flash('data saved', 'success')
        return redirect(url_for('result'))
    return render_template('classification.html', title='classification', form=form)


@app.route("/result")
def result():
    user = User.query.order_by(desc(User.id)).first()
    image_file = url_for('static', filename='finger_pics/' + user.image_file)
    classifier = Classifier()
    result = classifier.predict(image_file)
    return render_template('result.html', title='result', image_file=image_file, user=user, result=result)