from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def mainPage():
    return render_template('index.html', all_friends = [])

# INSERT
@app.route('/friends', methods=['POST'])
def create():
    print "*" * 50
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    print "*" * 50
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:firstname, :lastname, :occupation, NOW(), NOW())"
    data = {
        'firstname':request.form['first_name'],
        'lastname':request.form['last_name'],
        'occupation':request.form['occupation']
     }
    mysql.query_db(query,data)
    return redirect('/')

# UPDATE
@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name =: firstname, last_name =:lastname, occupation=:occupation WHERE ID = :id"
    data = {
        'firstname':request.form['first_name'],
        'lastname':request.form['last_name'],
        'occupation':request.form['occupation']
        'id': friend_id
     }
    mysql.query_db(query,data)
    return redirect('/')

# DISPLAY INFO
@app.route('/friends/<friend_id>')
def index(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id} # adding to key
    friend = mysql.query_db(query, data) # pass in query to db call
    print "*" * 50
    print friend
    print "*" * 50
    print "*" * 50
    print friend[0]
    print "*" * 50
    return render_template('index.html', all_friends = friend[0])

app.run(debug=True)
