# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from flask import render_template, flash, redirect, request, url_for
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, UploadDatasetForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, House
from datetime import datetime
from werkzeug.utils import secure_filename
import os
from app.utilities import convert_uploaded_csv_to_dataframe

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
def index():
    # return "Привіт, світ!"
    return redirect(url_for('profile', user_id=current_user.id))

@app.route('/profile/<user_id>')
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html',
                           title='User profile',
                           user=user,
                           houses=user.houses)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email address or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/upload_dataset', methods=['GET', 'POST'])
@login_required
def upload_dataset():
    form = UploadDatasetForm()
    if form.validate_on_submit():
        df = convert_uploaded_csv_to_dataframe(request.files)
        houses = []
        for index, row in df.iterrows():
            h = House(MSZoning=row['MSZoning'],
                      LotArea=row['LotArea'],
                      SalePrice=row.get('SalePrice', default=0),
                      user_id=current_user.id)
            houses.append(h)

        db.session.bulk_save_objects(houses)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('upload_dataset.html', form=form)
