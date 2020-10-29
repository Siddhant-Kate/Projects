from app import *
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request, session
from models import * 

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/fill')
def fill():
    return render_template('fill.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', user = user)

@app.route('/register')
def register():
    return render_template('register.html')

