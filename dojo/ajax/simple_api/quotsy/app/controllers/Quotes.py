from system.core.controller import *
import logging
#import re
#from flask import flash

class Quotes(Controller):

    def __init__(self, action):
        logging.debug("init:begin")
        super(Quotes, self).__init__(action)

        self.load_model('Quote')
        self.db = self._app.db

    def index(self):
        quotes = self.models['Quote'].all()
        return self.load_view('quotes/index.html', quotes=quotes)

    def index_json(self):
        """ Get quotes in json format """
        quotes = self.models['Quote'].all()
        return jsonify(quotes=quotes)

    def index_html(self):
        """ Get quotes as html partial """
        quotes = self.models['Quote'].all()
        return self.load_view('partials/quotes.html', quotes=quotes)

    def create(self):
        """ create a new quote """
        new_quote = {
            "author" : request.form['author'],
            "quote"  : request.form['quote']
        }
        self.models['Quote'].create(new_quote)
        quotes = self.models['Quote'].all()
        return self.load_view('partials/quotes.html', quotes=quotes) # redirect('/')
