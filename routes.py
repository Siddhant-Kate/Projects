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

@app.route('/login', methods=['POST', 'GET'])
def login():
    user_name = request.form.get('username')
    pass_word = request.form.get('password')

    user_details = User.query.filter(User.username==user_name).first()

    if user_details is None:
        print("Yall fucked up")
        return render_template('login.html')
    
    if user_details:
        return render_template('index.html')
    
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', user = user)

@app.route('/register')
def register():
    return render_template('register.html')

