from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from app import app, db
from app.models import User
from werkzeug.security import check_password_hash

@app.route('/')
def index():
    # Redirect to the login page by default
    return redirect(url_for('login'))

@app.route('/home')
def home():
    # Render the home page
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()  # Get user by username

        if user and check_password_hash(user.password, password):  # Check credentials
            login_user(user)  # Log in the user
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to home page
        else:
            flash('Invalid username or password.', 'danger')  # Error message

    # Render the login form
    return render_template('register.html')  # Change to 'login.html' for the login form

@app.route('/logout')
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out.', 'info')  # Display a message
    return redirect(url_for('login'))  # Redirect to login page

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        # Create a new user and hash the password
        new_user = User(username=username)
        new_user.setPassword(password)  # Hash the password

        db.session.add(new_user)  # Add the new user to the session
        db.session.commit()  # Commit the session to the database
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')  # Render the registration form
