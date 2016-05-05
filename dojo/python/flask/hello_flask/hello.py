from flask import Flask, render_template
app = Flask(__name__)

# index - home
@app.route('/')
def helloWorld():
    #return app.root_path
    return render_template('index.html', name="Chris")

# success
@app.route('/success')
def success():
        return render_template('success.html')
# contact info
@app.route('/info')
def info():
    return ("my contact info")
app.run(debug=True)
