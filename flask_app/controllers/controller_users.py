from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User

@app.route('/')
def login_page():
    session.clear()
    # session['user_id'] = 1
    return render_template('landing.html')

@app.route('/user/create', methods =["POST"])
def write_user():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        **request.form,
        'password': pw_hash
    }
    user_id = User.write_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/user/login', methods=["POST"])
def login():
    email = request.form['email']
    user_exist = User.login(email)
    if not user_exist:
        flash("Invalid Email or Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_exist.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect('/')
    session['user_id'] = user_exist.id
    return redirect('/dashboard')

@app.route('/user/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect('/')