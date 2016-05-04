from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

# COUNT BY 1
@app.route('/')
def index():
    # all values are stored as strings in a dictionary, must cast to number
    if "count" in session:
        count = int(session['count'])
        count += 1
    else:
        count = 0 # set init value
        session['count'] = count

    session['count'] = count # save count for next pass
    return render_template('index.html', count=session['count'])

# INCREMENT COUNT BY TWO
@app.route('/double')
def incrByTwo():
    count = int(session['count'])
    count += 2
    session['count'] = count
    return render_template('index.html', count=session['count'])

# RESET COUNT
@app.route('/reset')
def resetCount():
    if 'count' in session:
        del session['count']
    return redirect('/')

app.run(debug=True)
