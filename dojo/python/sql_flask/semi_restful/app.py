"""
app.py: demonstrating semi-restful
Author: Guy Whorley
"""
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import bcrypt

import time
import re  # Regular Expressions

app = Flask(__name__)

'''
Route Intecept and URL bindings
'''
@app.route('/')
def index():

	now = time.localtime()
	time.strftime('%Y-%m-%d %A', now)

	# return "You've reached the index page."
	return render_template('index.html', now = now)

@app.route('/login', methods=['POST'])
def login(): pass

@app.route('/logout')
def logout(): pass

@app.route('/user/<username>')
def profile(username): pass



if __name__ == '__main__':
	app.debug = True	# reload app on code changes; debug messages
	# app.run(host='0.0.0.0') # visible on network
	app.run(
		port = 9001
	) 				# only on localhost
