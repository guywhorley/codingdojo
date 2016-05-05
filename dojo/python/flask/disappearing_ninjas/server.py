from flask import Flask, render_template, request, redirect, session, flash
import re #regEx

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def noNinjas():
    return render_template('index.html')

@app.route('/ninja')
def fourNinjas():
    return render_template('four.html')

@app.route('/ninja/<color>')
def showNinjas(color):
    return render_template('showninjas.html', color=color)

app.run(debug=True)
