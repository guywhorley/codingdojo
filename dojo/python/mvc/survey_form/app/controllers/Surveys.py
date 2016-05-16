"""
    Surveys Controller - processes user surveys.
"""
from system.core.controller import *
from gutils.glog import *

class Surveys(Controller):

    def __init__(self, action):
        super(Surveys, self).__init__(action)

        # check and init counter
        if not 'counter' in session:
            session['counter'] = 0

        self.load_model('MainModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def process(self):
        # logging.debug('process:begin')
        session['counter'] += 1

        logging.debug('About to get form data...')

        # grab form data
        session['name'] = request.form['name'].strip()
        session['language'] = request.form['favlanguage']
        session['location'] = request.form['favlocation']
        session['comment'] = request.form['comments'].strip()
        logging.info('FORM DATA = "{}, {}, {}, {}"'.format(session['name'], session['location'], session['language'], session['comment']))

        # logging.debug('process:end')
        return redirect('/result')


    def result(self):
        return self.load_view('results.html')
