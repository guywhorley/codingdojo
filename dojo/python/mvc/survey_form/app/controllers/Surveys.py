"""
    Surveys Controller - processes user surveys.
"""
from system.core.controller import *
from gutils.glog import *

cn = "Surveys"

class Surveys(Controller):

    def __init__(self, action):
        glogDebug("Enter {}#__init__()...".format(cn))
        super(Surveys, self).__init__(action)
        glogSetLogLevel = 0

        # check and init counter
        if not 'counter' in session:
            session['counter'] = 0

        self.load_model('SurveysModel')
        self.db = self._app.db
        glogDebug("...exit {}#__init__()".format(cn))

    def index(self):
        glogDebug("Enter {}#index()...".format(cn))

        glogDebug("...exit {}#index()".format(cn))
        return self.load_view('index.html')

    def process(self):
        glogDebug("Enter {}#process()...".format(cn))

        session['counter'] += 1

        glogDebug("...exit {}#process()".format(cn))
        return redirect('/result')

    def result(self):
        glogDebug("Enter {}#result()...".format(cn))


        glogDebug("...exit {}#result()".format(cn))
        return self.load_view('results.html')

    # def clear(self):
    #     session['counter'] = 0
    #     return self.load_view('index.html')
