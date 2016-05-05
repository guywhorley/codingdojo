from flask import Flask, render_template, request, redirect, session, flash
import re #regEx

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
#end def

@app.route('/process', methods=['POST'])
def process():
    # do val here
    if len(request.form['email']) < 1:
        flash("email cannnot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("invalid Email Address!")
    else:
        flash("Success! Your name is {}".format(request.form['name]']))
    return redirect('/')

app.run(debug=True)
