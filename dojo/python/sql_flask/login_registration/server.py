from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
  # Begin my code here

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, "mordor_registration")

# regex patterns for checking user input
NAME_REGEX = re.compile('^.[1,45]$[a-zA-Z]') # name regex- no spaces, no numbers, at least 2 chars
PASSWORD_REGEDX = re.compile('^[a-zA-Z0-9]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# POST-LOGIN HOME
@app.route('/')
def index():
  # Check if session contains user_id: if not, go to login page
  #session['user_id'] = 1;
  if not 'user_id' in session:
    return redirect('/login')
  return render_template('/index.html')

# LOGIN
@app.route('/login')
def login():
  return render_template('login.html')

# PROCESS LOGIN
@app.route('/processLogin', methods=['POST'])
def processLogin():
  # Validate email and check passwords match, else show error messages and redirect to /showLogin
  session['user_id'] = 3
  if session['user_id'] == 5:
    return redirect('/')
  else:
    session['view'] = "alert"
    flash("Login failed! Did you use the right email and password? Are you registered yet?")
  return redirect('/login')

# REGISTER
@app.route('/register', methods=['POST','GET'])
def register():
  # Add user to database if not already present
  # Note: since email is unique, insert will fail if email is present.
  # try:
  #   pass
  # except Exception as e:
  #   raise
  #   # user email is already in system.
  #   return redirect('/register')
  return render_template('register.html')

@app.route('/processRegister', methods=['POST'])
def registerNewUser():
  # Add user to database and log user in
  session['user_id'] = 1 # TESTING
  return redirect('/')

@app.route('/logout')
def logout():
  #remove user_id from session
  del session['user_id']
  return redirect('/')

app.run(debug=True)
