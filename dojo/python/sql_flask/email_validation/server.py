from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def mainPage():

    return render_template('index.html')

# INSERT EMAIL
@app.route('/processEmail', methods=['POST'])
def createNewEmail():

    session['view'] = "alert"

    if len(request.form['email']) < 1:
        flash("Email cannnot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("The email address you entered, {}\nis a valid email address. Thank you.".format(request.form['email']))
        session['view'] = "success"

    if (session['view']=="success"):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email':request.form['email']
        }
        mysql.query_db(query,data)
        print session['view']
    return redirect('/')

app.run(debug=True)
