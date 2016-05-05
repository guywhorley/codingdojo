from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "SecretWorld"
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def showResults():
    valOkay = True

    # form validation
    if (len(request.form['name'])) < 1:
        flash("Name cannot be empty!")
        valOkay = False
    elif (len(request.form['comments'])) < 1:
        flash("Comments cannot be empty!")
        valOkay = False
    elif (len(request.form['comments'])) > 120:
        flash("Comments cannot be longer that 120 characters!")
        valOkay = False

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    # decide on where to go based on flag
    if (valOkay):
        return render_template("results.html", name=name, location=location, language=language, comments=comments)
    else:
        return redirect('/')
    #return redirect(page)
app.run(debug=True) # run our server
