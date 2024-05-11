from project import app
from flask import render_template , redirect , url_for , flash , get_flashed_messages
from project.models import User
from project.forms import RegisterForm , LoginForm
from project import db
from flask_login import login_user , logout_user
from project.forms import LoginForm
from flask_login import current_user
from flask_login import login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')




@app.route('/dashboard')
def DashBoard():
    if not current_user.is_authenticated:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login_page'))

    return render_template('dashboard.html')






@app.route('/about')
def About_page():
    
    return render_template('About.html') 

@app.route('/register', methods=['GET', 'POST'])    
def register_page():
    form = RegisterForm()
    
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit() 
        login_user(user_to_create)
        
        flash('Account created successfully!', 'success')
        return redirect(url_for('DashBoard'))
    if form.errors != {}: #if there r no errors from the validation 
        for err_msg in form.errors.values():
            flash(f'There was an error when creating user: {err_msg}' , category='danger')  # <- Correct indentation
    
    return render_template('register.html', form=form)  # <- Correct indentation

from flask import flash


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password_correction(form.password.data):  # Using the method to check password
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('DashBoard'))
            else:
                flash('Incorrect password. Please try again.', category="danger")
        else:
            flash('User not found. Please check your username.', category="danger")
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!" , category='info')
    return redirect(url_for('login_page'))