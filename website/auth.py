from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/about_info', methods=['GET', 'POST'])
def about_info():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
        
    return render_template("info.html")
    
@auth.route('/project', methods=['GET', 'POST')
def project():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
        
    return render_template("projects.html")
        
@auth.route('/help',  methods=['GET', 'POST'])
def help():
    data = request.form
    print(data)

    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')
        
        if len(email) < 5:
            flash('An Email must have more than 5 characters.', category = 'error')
            
        elif len(message) < 2:
            flash('The message text must have more than 1 characters.', category = 'error')
            
        else:
            flash('Your message has been sent succesfully.')
            
    return render_template("help.html")
