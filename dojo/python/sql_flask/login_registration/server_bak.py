from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt(Bcrypt(app)
# app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app, 'friendsdb') # DATABASE

NAME_REGEX = re.compile('^[a-zA-Z]') # name regex- no spaces, no numbers

PASSWORD_REGEDX = re.compile('^[a-zA-Z0-9]')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

# **************
#  LOGIN
# **************
@app.route('/login', methods=['POST']
def login():
  email = request.form['email']
  username = request.form['username']
  password = request.form['password']
  pw_hash = bcrypt.generate_password_hash(password) # generate hash

  query = "SELECT  * FROM users WHERE email = :email LIMIT 1"
  data = {
    'email': email
  }
  user = mysql.query_db(query, data)
  # the check_password_hash compares encr-val with unencr pwd
  if (bcrypt.check_password_hash(user[0]['pw_hash'], password):
    # login
else:
    # set flash error

  #return


# *****************
#  CREATE NEW USER
# *****************
@add.route('/create_user', methods=['POST'])
def create_user():
  email = request.form['email']
  username = request.form['username']
  password = request.form['password']
  pw_hash = bcrypt.generate_password_hash(password) # generate hash
  query = "INSERT INTO users (email, username, pw_hash, created_at) VALUES (:email, :username, :pw_hash, NOW())"
  query_data = {
    'email': email,
    'username': username,
    'pw_hash': pw_hash
  }
  mysql.query_db(query, query_data)
  # redirect to success page
  return redirect('/')

# # DISPLAY ALL FRIENDS *** IS WORKING! DO NOT TOUCH THIS ***
# @app.route('/', methods=['POST', 'GET'])
# def index(): # handler function
#     friends = [] # init empty friend
#     try:
#         query = "SELECT * FROM friends"
#         friends = mysql.query_db(query)
#     except Exception as e:
#         flash("Friends are having issues. Try back later.")
#     return render_template('index.html', all_friends=friends)
#
# # DISPLAY SINGLE USER RECORD - *** IS WORKING! DO NOT TOUCH ***
# @app.route('/friends/<id>/edit', methods=['POST','GET'])
# def edit(id):
#     try:
#         # auto-populate the form
#         query = "SELECT * FROM friends WHERE id = :specific_id"
#         data = {'specific_id': id} # adding to key
#         friend = mysql.query_db(query, data) # pass in query to db call
#     except:
#             flash( "Unable to edit Friend ID: {0}!".format(id))
#     return render_template('edit.html', all_friends = friend[0])
#
# # PROCESS UPDATES
# @app.route('/friends/<id>', methods=['POST'])
# def update(id):
#     valOK = False;
#     session['view'] = "alert"
#
#     if len(request.form['fname']) < 1:
#         flash("First name cannnot be empty!")
#     elif not NAME_REGEX.match(request.form['fname']):
#         flash("First name can only contain letters!")
#     elif len(request.form['lname']) < 1:
#         flash("Last name cannnot be empty!")
#     elif not NAME_REGEX.match(request.form['lname']):
#         flash("Last name can only contain letters!")
#     elif len(request.form['occ']) < 1:
#         flash("Occupation cannnot be empty!")
#     elif not NAME_REGEX.match(request.form['occ']):
#         flash("Occupation can only contain letters!")
#     else:
#         valOK = True
#     # Update the record if fields pass all validation
#     if (valOK):
#         try:
#             query = "UPDATE friends SET first_name ='" + request.form['fname'] + "', last_name='" + request.form['lname'] + "', occupation='" + request.form['occ'] + "', updated_at=NOW() WHERE ID = " + id
#             mysql.query_db(query)
#             session['view'] = "success"
#             flash("Sucessfully changed ID " + id)
#         except Exception as e:
#             session['view'] = "alert"
#             flash("Unable to change your friend!")
#             return redirect('/friends/' + id + '/edit')
#     else:
#         return redirect('/friends/' + id + '/edit')
#     return redirect('/')
#
# #  DELETE RECORD - *** IS WORKING! DO NOT TOUCH THIS ***
# @app.route('/friends/<id>/delete')
# def destroy(id):
#     try:
#         query = "DELETE FROM friends WHERE ID = :id"
#         data = { 'id': id }
#         mysql.query_db(query,data)
#     except Exception as e:
#         flash( "Unable to delete Friend ID: {0}!".format(id))
#         print e
#     return redirect('/')
#
# # CREATE NEW FRIEND
# @app.route('/create')
# def create():
#     return render_template('add.html')
#
# # CREATE NEW FRIEND
# @app.route('/friends', methods=['POST'])
# def saveFriend():
#
#     fname = request.form['fname']
#     lname = request.form['lname']
#     occ   = request.form['occ']
#
#     valOK = False;
#     session['view'] = "alert"
#
#     if len(fname) < 1:
#         flash("First name cannnot be empty!")
#     elif not NAME_REGEX.match(fname):
#         flash("First name can only contain letters!")
#     elif len(lname) < 1:
#         flash("Last name cannnot be empty!")
#     elif not NAME_REGEX.match(lname):
#         flash("Last name can only contain letters!")
#     elif len(occ) < 1:
#         flash("Occupation cannnot be empty!")
#     elif not NAME_REGEX.match(occ):
#         flash("Occupation can only contain letters!")
#     else:
#         valOK = True
#     # Update the record if fields pass all validation
#     if (valOK):
#         try:
#             query = "INSERT INTO friends"
#             query = query + " (first_name, last_name, occupation, created_at, updated_at)"
#             query = query + " VALUES('" + fname + "','" + lname + "','" + occ + "', NOW(), NOW())"
#             mysql.query_db(query)
#             session['view'] = "success"
#             flash("Sucessfully added new friend")
#         except Exception as e:
#             session['view'] = "alert"
#             flash("Unable to add new friend!")
#             return redirect('/create')
#     else:
#         return redirect('/create')
#     return redirect('/')

app.run(debug=True)
