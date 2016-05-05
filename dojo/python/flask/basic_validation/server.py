from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/') # initialize game state
def index():
    return render_template('index.html')
#end def

@app.route('/process', methods=['POST'])
def process():
    # do val here
    if len(request.form['name']) < 1:
        flash("Name cannnot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form['name]']))
    return redirect('/')

app.run(debug=True)
