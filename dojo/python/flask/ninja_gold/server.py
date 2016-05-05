from flask import Flask, render_template, request, redirect, session
import random, datetime, time

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/') # initialize game state
def index():
    log = []
    if "log" not in session:
        log.append("started gathering gold.")
        session['log']= log

    if "gold" not in session:
        session['gold'] = 0

    return render_template('/index.html')
#end def

@app.route('/process_money', methods=['POST'])
def processMoney():

    log = session['log'] # log array

    # determine ops and gold loss/won
    intGold = int(session['gold']) # str -> int

    # get NOW()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    if (request.form['building'] == 'farm'):
        coin = getRandomGold(10,20)
        message = "Earned " + str(intGold) + " from the farm! (" + now + ")"
    elif (request.form['building'] == 'cave'):
        intGold += getRandomGold(5,10)
        message = "Earned " + str(intGold) + " from the cave! (" + now + ")"
    elif (request.form['building'] == 'house'):
        intGold += getRandomGold(2,5)
        message = "Earned " + str(intGold) + " from the house! (" + now + ")"
    elif (request.form['building'] == 'casino'):
        intGold += getRandomGold(-50,50)
        message = "Earned " + str(intGold) + " from the casino! (" + now + ")"

    log.insert(0, message) # insert current message to head
    session['log'] = log # save log arrray
    session['gold'] = str(intGold) # save players new gold total

    return redirect('/')
#end def

def getRandomGold(startVal, endVal):
    return random.randint(startVal, endVal)

app.run(debug=True)
