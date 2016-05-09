from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "walldb")

# My Regex Patters
NAME_REGEX = re.compile('^[a-zA-Z].{1,45}$') # name regex- no spaces, no numbers, at least 2 chars
PASSWORD_REGEDX = re.compile('^[a-zA-Z0-9].{7,45}$') # must be 8 or more characters in length
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Registration Information Landing Page; you only see this if are have
# registered and logged in succesfully. User_ID will have already been inserted into session.
@app.route('/')
def index():
	if not 'user_id' in session:
		return redirect('/login')
	else: # grab user information to populate home page
		user = getUserInfo(session['session_id'])
		fname = user[0]['first_name']
		lname = user[0]['last_name']
		email = user[0]['email']
		regDate = user[0]['created_at']
		lastUpd = user[0]['updated_at']
	return redirect('/theWall')

# Add comment to a postMessage
@app.route('/comment/<id>/<orig_author_id>')
def commentOnPost(id, orig_author_id):
	if not 'session_id' in session:
		session['view'] = "alert"
		flash("There's a problem! I didn't recognize your id.")
		return redirect('/login')
	else:
		# get currently logged-in user
		user = getUserInfo(session['session_id'])
		fname = user[0]['first_name']
		lname = user[0]['last_name']

		# Get original message and place text on top...
		query = "SELECT messages.user_id,users.first_name, users.last_name, messages.message, DATE_FORMAT(messages.created_at,'%a, %b %D %Y @%T') AS created_at, messages.id FROM messages JOIN users ON messages.user_id = users.id WHERE messages.id = :id ORDER BY messages.created_at DESC LIMIT 1"
		data = { 'id':  id }
		post = mysql.query_db(query, data)

		post_fname = post[0]['first_name']
		post_lname = post[0]['last_name']
		post_cat = post[0]['created_at']
		post_msg = post[0]['message']
		post_msg_id =id

	return render_template('/comment.html', fname = fname,  lname = lname, commentor_id = session['session_id'], post_msg_id = post_msg_id, post_fname = post_fname, post_lname = post_lname, post_cat = post_cat, post = post_msg, messages = [])

# Show user wall with messages
@app.route('/theWall', methods=['POST','GET'])
def showTheWall():
	if not 'session_id' in session:
		session['view'] = "alert"
		flash("There's a problem! I didn't recognize your id.")
		return redirect('/login')
	else:
		user = getUserInfo(session['session_id'])
		fname = user[0]['first_name']
		lname = user[0]['last_name']
		email = user[0]['email']
		regDate = user[0]['created_at']
		lastUpd = user[0]['updated_at']

		# build the wall: get all messages
		query = "SELECT messages.user_id, users.first_name, users.last_name, messages.message, DATE_FORMAT(messages.created_at,'%a, %b %D %Y @%T') AS created_at, messages.id FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
		messages = mysql.query_db(query)

		# grab all comments associated with each message: iterate through messages and run the query
		#
		#     all_comments = [
		#   	{ 'post.id': [ {comment-1}, {comment-2}, {comment-3}] },
		#	 	{ 'post.id': [ {comment-1}, {comment-2}, {comment-3}] },
		#	 	{ ... }
		#	   ]
		#   where each comment is encapuslated as an array of dictionary objects,
		#	   { 'comment': c.comment, 'created_at': created_at, 'u.fname': u.fn, 'u.lname': u.ln }
		#
		all_comments = []
		for message in messages:
			# cm_query = "SELECT u.first_name, u.last_name, c.comment, date_format(c.created_at,'%a, %b %d %Y %T') AS created_at from comments AS c join users AS u on c.user_id = u.id where c.message_id = :id ORDER BY c.created_at DESC"
			cm_query = "SELECT u2.first_name, u2.last_name, c.comment, date_format(c.created_at,'%a, %b %d %Y %T') AS created_at from comments AS c join users AS u on c.user_id = u.id join users AS u2 on c.user_id = u2.id where c.message_id = :id ORDER BY c.created_at DESC"
			cm_data = { 'id': message['id'] }
			# select all comments related to messages and build master collection
			temp = mysql.query_db(cm_query, cm_data)
			if len(temp) > 0:
				comArr = []
				for i in range(len(temp)):
					comment = temp[i] # current single comment record
					buildIt = {}
					buildIt = {
						'comment': comment['comment'],
						'created_at': comment['created_at'],
						'u.fname': comment['first_name'],
						'u.lname': comment['last_name']
					}
					# bundle all post comments into one array
					comArr.append(buildIt)
				postD = {} # create a temp dictionary
				# postD[str(message['id'])] = comArr
				postD['id'] = message['id'] # associate key 'id' to actual id value
				postD['comments'] = comArr # assocaite key 'comments' to array
				all_comments.append(postD) # store the temp d in the all_commments array
		#print all_comments

	return render_template('/wall.html', fname=fname, lname=lname, email=email, regDate = regDate, lastUpd = lastUpd, posts = messages, comments = all_comments)
#
# Write message to DB
@app.route('/postMessage', methods=['POST'])
def postMessage():
	if (len(request.form['content']) < 1):
		session['view'] = "warning"
		flash("FYI: You didn't include any text in your post so I didn't save it.")
	else:
		query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:msg, NOW(), NOW(), :u_id)"
		data = { 'msg': request.form['content'], 'u_id' : session['session_id'] }
		mysql.query_db(query, data)
	return redirect('/theWall')

# Add Comment to database
@app.route('/submitComment', methods=['POST'])
def submitComment():
	if (len(request.form['comment']) < 1):
		session['view'] = "warning"
		flash("FYI: You didn't include any text in your comment so I didn't save it.")
	else:
		query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :u_id, :m_id)"
		data = {
			'comment': request.form['comment'],
			'u_id': session['session_id'],  #request.form['user_id'], #USE CURRENTLY LOGGED-IN USER
			'm_id': request.form['message_id']
		}
		mysql.query_db(query, data)
	return redirect('/theWall')

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
		flash("I didn't recognize that email. Try again.")
		return redirect('/login')

	user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	query_data = { 'email': email }
	user = mysql.query_db(user_query, query_data)
	if not user: # email was not found - user is null/empty
		session['view'] = "alert"
		flash("That email does not exist! Sign-up now for a free account @theWall.")
	else:
		if bcrypt.check_password_hash(user[0]['password'], password):
			session['session_id'] = user[0]['id']
			return redirect('/theWall')
		else:
			session['view'] = "alert"
			flash("Incorrect Password!")
	return redirect('/login')

# Spawn the register page
@app.route('/register', methods=['POST','GET'])
def register():
  return render_template('register.html')

# Handle the Registering: param checks and INSERT into DB
@app.route('/processRegister', methods=['POST'])
def registerNewUser():
	valOK = False;
	alertMsg = "(must be 2+ letters, no numbers, no specials characters)"
	session['view'] = "alert"
	if not NAME_REGEX.match(request.form['fname']):
		flash("First name is too short " + alertMsg)
	elif not NAME_REGEX.match(request.form['lname']):
		flash("Last name is too short " + alertMsg)
	elif len(request.form['email']) < 1:
		flash("Email cannnot be empty!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email format. Please use correct email address!")
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
	except:
		# User-provided email is not in database. We can add it now...
		fname = request.form['fname']
		lname = request.form['lname']
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		# INSERT NEW USER INTO DB
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :pwd, NOW(), NOW())"
		data = { 'first': fname, 'last': lname, 'email': request.form['email'], 'pwd': pw_hash }
		mysql.query_db(query,data)

		session['view'] = "success"
		flash("{} {}, You have sucessfully registered!".format(fname, lname))
		session['session_id'] = getID(email)
		return redirect('/theWall') # Go to landing page and show registration info.

	return redirect('/register') # failed to add user for any number of reasons.

@app.route('/logout')
def logout():
  	#remove user_id from session
	if 'user_id' in session:
		del session['session_id']
  	return redirect('/')

# Return user data for given ID
def getUserInfo(id):
	try:
		id = session['session_id']
		user_query = "SELECT * FROM users WHERE ID = :id LIMIT 1"
		query_data = { 'id': id }
		my_user = mysql.query_db(user_query, query_data)
		return my_user
	except:
		session['view'] = "alert"
		flash("I wasn't able to get your user information!")
	return False;

# Query users table with valid Email to get ID
def getID(validEmail):
	user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	query_data = { 'email': validEmail }
	user = mysql.query_db(user_query, query_data)
	return user[0]['id']

app.run(debug=True)
