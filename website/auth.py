from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
        
    return render_template("login.html")
    
    
@auth.route('/logout')
def logout():
    return render_template("logout.html")
        
        
@auth.route('/help',  methods = ['GET', 'POST'])
def help():
    data = request.form
    print(data)

    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')
        
        if len(email) < 5:
            flash('Email must be greater than 5 characters.', category = 'error')
            
        elif len(message) < 2:
            flash('The message must be greater than 2 characters.', category = 'error')
            
        else:
            flash('message sent succesfully')
            
    return render_template("help.html")
    


