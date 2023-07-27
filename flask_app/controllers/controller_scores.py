from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_scores import Scores
from flask_app.models.model_user import User
from flask_app.models.model_lifts import Lifts

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    rolling_high = Scores.get_10_scores()
    user_recent = Scores.get_user_10_scores(session['user_id'])
    all_scores = Scores.get_all_scores()
    user = User.get_one(session['user_id'])
    return render_template('dashboard.html', rolling_high = rolling_high, user_recent = user_recent, all_scores = all_scores, user = user)

@app.route('/view/detail/<int:id>')
def detail_view(id):
    lift = Scores.build_scorecard(id)
    return render_template('view_lift.html', lift = lift)

@app.route('/user/write_score', methods=["POST"])
def write_score():
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Scores.write_new_score(data)
    return redirect('/user/record')

@app.route('/user/record')
def record_lift():
    user = User.get_one(session['user_id'])
    lifts = Lifts.get_all()
    return render_template('record_lift.html', user = user, lifts = lifts)

@app.route('/user/view_edit/<int:id>')
def edit_score(id):
    score = Scores.get_score(id)
    lifts = Lifts.get_all()
    return render_template('edit_lift.html', score = score, lifts = lifts)

@app.route('/user/write_edit/', methods=["POST"])
def write_edit():
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Scores.edit_score(data)
    return redirect('/dashboard')

@app.route('/user/delete_score/<int:id>')
def delete_score(id):
    Scores.delete_score(id)
    return redirect('/dashboard')