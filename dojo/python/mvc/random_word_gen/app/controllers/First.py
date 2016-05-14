""" Sample Controller File
    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.
    Create a controller using this template
"""
from system.core.controller import *
from gutils.glog import *
import datetime
import random
from random import randrange

class First(Controller):

    def __init__(self, action):
        super(First, self).__init__(action)
        self.load_model('FirstModel')
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
        glogDebug("Enter index() ...")
        self.__addSession__()
        session['rndword'] = self.__generateRandomWord__(14,14)
        glogDebug("rndword: {}".format(session['rndword']))

        glogDebug("... exit index()")
        return self.load_view('index.html')

    def process(self):
        glogDebug("Enter process('/') ...")

        # save count and random word in session object
        session['rndword'] = self.__generateRandomWord__(14,14)
        session['id'] += 1

        glogDebug("... exit process('/')")
        return redirect('/')

    def __addSession__(self):
        # if session['id'] exists: then noop
        # else: add key 'id' to session, set id = 0; using id as counter
        glogDebug("Enter __addSession__() ...")
        if not (self.__isInSession__()):
            glogDebug("Adding session['id'] = 0")
            session['id'] = 0
        glogDebug("... exit __addSession__()")
        #end def

    def __generateRandomWord__(self, min, max):
        glogDebug("Enter __generateRandomWord__() ...")

        myText = ''
        choice = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9']

        for i in range(0, max):
            random_index = randrange(0,len(choice))
            myText += choice[random_index]

            # myText += random.choice(choice)
        glogInfo(myText)
        glogDebug("... exit __generateRandomWord__()")
        return myText

    def __isInSession__(self):
        glogDebug("Enter __isInSession__() ...")
        if 'id' in session:
            glogDebug("session['id'] exists")
            glogDebug("... exit __isInSession__():true")
            return True
        glogDebug("... exit__isInSession__():false")
        return False
