from flask import Flask, render_template, request, redirect, session, flash
import re #regEx

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/') # methods=['GET'])
def index():
    return render_template('index.html')
#end def

@app.route('/process', methods=['POST'])
def process():
    print "In process now."
    # check all of the given conditions
    if len(request.form['email']) < 1:
        flash("email cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("invalid Email Address!")
    elif len(request.form['fname']) < 1:
        flash("First name cannot be empty!")
    elif not (request.form['fname'].isalpha()):
        flash("First name cannot contain any numbers!")
    elif len(request.form['lname']) <1:
        flash("Last name cannot be empty!")
    elif not (request.form['lname'].isalpha()):
        flash("Last name cannot contain any numbers!")
    elif len(request.form['pwd']) < 8:
        flash("Password must be at least 8 characters long!")
    elif not( request.form['pwd'] == request.form['cpwd']):
        flash("Passwords do not match each other!")
    else:
        flash("success")
    return redirect('/')

app.run(debug=True)
