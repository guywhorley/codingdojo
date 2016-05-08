from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "mordor_registration")

# My Regex Patters
NAME_REGEX = re.compile('^[a-zA-Z].{1,45}$') # name regex- no spaces, no numbers, at least 2 chars
PASSWORD_REGEDX = re.compile('^[a-zA-Z0-9].{7,45}$') # must be 8 or more characters in length
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Registration Information Landing Page; you only see this if are have
# registerd and logged in succesfully. User_ID will have already been inserted into session.
@app.route('/')
def index():
    if not 'user_id' in session:
        return redirect('/login')
    else:
        # grab user information to populate home page
        id = session['user_id']
        user_query = "SELECT * FROM users WHERE ID = :id LIMIT 1"
        query_data = { 'id': id }
        user = mysql.query_db(user_query, query_data)
        fname = user[0]['first_name']
        lname = user[0]['last_name']
        email = user[0]['email']
        regDate = user[0]['created_at']
    return render_template('/index.html', fname=fname, lname=lname, email=email, regDate = regDate)

# Spawn the login page.
@app.route('/login')
def login():
    return render_template('login.html')

'''
Process Login: Validate email and check that passwords match, else show error
messages and redirect to login page. '''
@app.route('/processLogin', methods=['POST'])
def processLogin():
    email = request.form['email']
    password = request.form['password']
    if not EMAIL_REGEX.match(request.form['email']):
        session['view'] = "alert"
        flash("I didn't recognize the email format. Try again.")
        return redirect('/login')

    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)
    if not user: # email was not found - user is null/empty
        session['view'] = "alert"
        flash("Email not registered!")
    else:
        if bcrypt.check_password_hash(user[0]['password'], password):
            session['user_id'] = user[0]['id']
            return redirect('/')
        else:
            session['view'] = "alert"
            flash("Incorrect Password!")
    return redirect('/login')

# Spawn the register page
@app.route('/register', methods=['POST','GET'])
def register():
  return render_template('register.html')

@app.route('/processRegister', methods=['POST'])
def registerNewUser():
    valOK = False;
    session['view'] = "alert"
    if not NAME_REGEX.match(request.form['fname']):
        flash("First name is too short (must be 2+ letters with no numbers or special characters")
    elif not NAME_REGEX.match(request.form['lname']):
        flash("Last name is too short (must be 2+ letters with no numbers or special characters")
    elif len(request.form['email']) < 1:
        flash("Email cannnot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email format. Please use correct email address.!")
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters!")
    elif (request.form['password'] != request.form['cpassword']):
        flash("Password confirmation does not match! Try again.")
    else:
        valOK = True
    if not (valOK): # Validation failed -- bail out!
        return redirect('/register')
    try: # check for pre-existing email
        email = request.form['email']
        query = "SELECT * FROM users WHERE email like '" + email + "' LIMIT 1"
        user = mysql.query_db(query)
        if (user[0]['password']): # if key is present, email already exists! If not, error is thrown.
            session['view'] = "alert"
            flash("Unable to register. Please use a different email.")
    except: # User-provided email is not in database. We can add it now...
        fname = request.form['fname']
        lname = request.form['lname']
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users"
        query = query + " (first_name, last_name, email, password, created_at, updated_at)"
        query = query + " VALUES('" + fname + "','" + lname + "','" + email + "','" + pw_hash + "', NOW(), NOW())"
        user = mysql.query_db(query)
        session['view'] = "success"
        flash("{} {}, You have sucessfully registered!".format(fname, lname))
        session['user_id'] = getID(email)
        return redirect('/') # Go to landing page and show registration info.
    return redirect('/register') # failed to add user for any number of reasons.

@app.route('/logout')
def logout():
  #remove user_id from session
  del session['user_id']
  return redirect('/')

# Query users table with valid Email to get ID
def getID(validEmail):
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': validEmail }
    user = mysql.query_db(user_query, query_data)
    return user[0]['id']

app.run(debug=True)
