""" Sample Controller File
    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.
    Create a controller using this template
"""
from system.core.controller import *
from gutils.glog import *
import datetime

class Welcome(Controller):

    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """ This is an example of a controller method that will load a view
        for the client """

    def index(self):
        """
        A loaded model is accessible through the models attribute self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        glogDebug("Enter index()...")

        glogDebug("Exit index()...")
        return self.load_view('index.html')

    def process(self):
        glogDebug("Enter process('/')...")
        glogInfo("Username:{}".format(request.form['name']))

        # save name in session object and goto success.html
        session['name'] = request.form['name']

        glogDebug("Exit process('/')")
        return redirect('/welcome/success')

    def success(self):
        return self.load_view('success.html', name=session['name'])
