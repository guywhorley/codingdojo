"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('SurveysModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def process(self):
        return redirect('/result')

    def result(self):

        return self.load_view('results.html')
