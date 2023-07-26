from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.model_lifts import Lifts


@app.route('/admin/new_lift_type')
def render_new_lift_type():
    # verify user is admin in here
    return render_template("new_lifttype.html")

@app.route('/admin/edit_lift_type/<int:id>')
def render_edit_lift_type(id):
    #verify user is admin here
    lift = Lifts.get_one(id)
    return render_template('/edit_lifttype.html', lift = lift)


@app.route('/admin/write_lift', methods=["POST"])
def admin_writelift():
    # verify user is admin in here
    Lifts.write_lift(request.form)
    return redirect('/admin/new_lift_type')

@app.route('/admin/edit_lift', methods=["POST"])
def admin_editlift():
    Lifts.edit_lift(request.form)
    return redirect('/dashboard')