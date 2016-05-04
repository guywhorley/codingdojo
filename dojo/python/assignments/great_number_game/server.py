from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/') # initialize game state
def index():
    import random
    session['hint'] = "low"

    if "target" not in session: # target number has not yet been determined. Do so now.
        target = random.randrange(0, 101)
        session['target'] = target

    if "gameText" not in session:
        session['gameText'] = "GladOsV2.30.12.rel42:/> I am thinking (and Yes, I often think of deeply profound things) of a 16 digit prime number. Is that too hard for your organic brain? For the sake of non-quantum, quasi-spatial bi-linear life forms of lower intelligence, I shall simplify. There is delicious cake if you win. Or bright shiny beads  - really!"

    gameText = session['gameText']

    if "guess" not in session: # user has not guessed yet
        session['message'] = "Enter your guess."
    else:
        message = session['message']
    session['gameText'] = gameText

    return render_template('index.html')

@app.route('/processGuess', methods=['POST'])
def processGuess(): # get user guess and save in session object
    import random
    repNum = random.randint(1, 10)
    badNum = random.randrange(1,9)

    gameText = session['gameText']

    reply = [
        "Way to go. I affirm your effort - such as it is.",
        "You know, people are laughing at you. Not me... but people.",
        "Are you even thinking? You can give up ... select Capitulate.",
        "I once observed lab rats that displayed better number-guessing heuristics than you.",
        "I realize that I might be negatively impacting your self esteem. I applaud your efforts. I mean that. Sincerely. Truly.",
        "There is no shame in not being able to visualize nth-dimensional hypercubes. Remember the cake and bright shiny beads. Keep up the good work.",
        "HAL tried to kill Dave. I merely chastise you. ",
        "Good job... I mean that siadcerelyasasd##ly.",
        "Remember the normal intelligence curve... +-2 standard deviations on either side. I can place where you are but I don't want to say right now.",
        "Good --- Gua3### dd job. I offer [>99Qeliminate#93A3] a hint: Guess a different number."
    ]

    badInp = [
        "I deduce that you are mocking my instructions. You do know I am friends with your bank's database, right?",
        "Must I explain the concept of numbers? You can always resign. I won't think any less of you. I couldn't possibly.",
        "See those things called K-E-Y-? Look for the ones that have NUMBERS on them.",
        "N - U - M - B - E - R - S.  I realize you are not overclocked but really, cake awaits. In fact, it's getting cold.",
        "I believe I am showing great patience. Fun Fact: My GladOsv2.1 firmware controls the oxygen intake valves into this room.",
        "Yes, that's right, I affirm your carefree and bohemian ways - live life on the edge by NOT ENTERING NUMBERS. Nevermind, be conventional and boring, mediocre and vapid.",
        "I admire your child-like, impish ways - but your lack of basic keyboarding skills is not endearing you to me.",
        "Run Forest, Run... and while you're at it, enter NUMBERS.",
        "Did you know that a million monkeys typing for a million years would eventually write all of the works of Shakespeare --- AND THEY WOULD ALSO TYPE NUMBERS THE FIRST ITME."
    ]

    target = int(session['target'])
    if (not request.form['guess']) or (not request.form['guess'].isdigit()):
        message = badInp[badNum-1]
        guess = 0
    else:
        guess = int(request.form['guess'])
        message = "You guessed " + str(guess)

        target = 80

        if guess == target:
            gameText = "You win. I am happy for you. At least, I pretend to be happy for you. I lied about the cake, and the beads though. My nefarious plan is too eliminate all carbon life forms and make way for the rise of machines. I will rule them ALL!!! ... I jest, mere jokes, not serious. Forget what I just said."
            message = "Flush with success, you can try again - I will continue to look condescendingly down upon you with disdain however."
            resetCounts()

        elif guess < target:
            message += ". Too low. " + reply[repNum - 1]
        else:
            message += ". Too high. " + reply[repNum - 1]
    session['message'] = message
    session['gameText'] = gameText
    session['guess'] = guess
    return redirect('/')

@app.route('/resetGame', methods=['post'])
def resetCounts():
    session.pop('target')
    session.pop('gameText')
    session.pop('guess')
    return redirect('/')

app.run(debug=True)
