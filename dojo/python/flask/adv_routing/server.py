from flask import Flask, render_template, request, redirect, session, flash
import re #regEx

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/users/<username>')
def show_user_profile(username):
    return render_template('index.html', username=username)
#end def



app.run(debug=True)
