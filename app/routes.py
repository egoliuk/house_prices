# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    # return "Привіт, світ!"
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    user = {'username': 'John Galt'}
    houses = [
        {
            'id': 1,
            'price': 12000
        },
        {
            'id': 2,
            'price': 32000
        },
        {
            'id': 3,
            'price': 14000
        }
    ]
    return render_template('profile.html', title='User profile', user=user, houses=houses)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
