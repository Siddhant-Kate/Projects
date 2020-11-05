from app import *
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request, session
from models import * 
from random import *

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
    if request.method == "POST":
        user_name = request.form.get('username')
        pass_word = request.form.get('password')

        user_details = User.query.filter(User.username==user_name).first()

        if user_details is None:
            print("Test line.")
            return render_template('login.html')
            
        if user_details:
            return render_template('index.html')
    
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', user = user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        u_name = request.form.get('username')
        p_word = request.form.get('password')
        cp_word = request.form.get('confirm_password')
        email = request.form.get('email')
        c_email = request.form.get('confirm_email')

        if u_name == None or p_word == None or c_email == None:
            return render_template('register.html')

        if email != c_email:
            flash("Your email id is not entered correctly.")
            return render_template('register.html')

        if p_word != cp_word:
            flash("Your password is not entered correctly.")
            return render_template('register.html')

        temp = User.query.filter(User.email==email).first()
        if temp:
            flash("This email id is already registered.")
            return render_template('register.html')

        temp = User.query.filter(User.username==u_name).first()
        if temp:
            flash("This username is already registered.")
            return render_template('register.html')

        new_id = randint(5, 1000)
        temp = User.query.filter(User.id==new_id).first()
        if temp is None:
            new_user = User(id=new_id, username=u_name, password=p_word, email=c_email)
            db.session.add(new_user)
            db.session.commit()
            flash("You have registered successfully.")
            return render_template('login.html')
    

    return render_template('register.html')

