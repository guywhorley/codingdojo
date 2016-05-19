from system.core.controller import *
import logging
import random
import datetime
import time

class Game(Controller):

    def __init__(self, action):
        logging.debug("init:begin")
        super(Game, self).__init__(action)
        # self.load_model('GameModel')
        self.db = self._app.db

    def index(self):
        logging.debug("index:begin")

        # set initial gold value
        if not 'gold' in session:
            session['gold'] = 0
            session['messages'] = []

        logging.debug("index:end")
        return self.load_view('index.html')

    def process_money(self, methods=['POST']):
        """ update money balance and set messages """
        ds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        logging.info("ds: {}".format(ds))

        updateAmount = 0
        gold = session['gold']
        venue = request.form['venue']
        messages = session['messages']

        if venue == 'farm':
            updateAmount = random.randint(10,21)

        elif venue == 'cave':
            updateAmount = random.randint(5,10)

        elif venue == 'house':
            updateAmount = random.randint(2,5)

        else: # is casino by process of elimination
            updateAmount = random.randint(-50,50)

        # construct message and add to messages
        if updateAmount < 0:
            message = 'Entered a {} and lost {} coins. Ouch!   {}'.format(venue, updateAmount, ds)
        else:
            message = "Earned {} from the {}!  {}".format(updateAmount,venue, ds)

        # save messages in session obj
        logging.info(message)
        messages.insert(0, message)

        # save gold in session obj
        gold += updateAmount
        session['gold'] = gold

        return redirect('/')
