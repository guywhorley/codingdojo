""" Sample Controller File
    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.
    Create a controller using this template
"""
from system.core.controller import *
import datetime

# Logging Utilities
# Guy Whorley
# Using ANSII Colors to print color console messages
# To enable various levels of log messages, set logLevel as follows:
#   logLevel = _NONE_ | _INFO_ | _ALL_
#   NOTE: Error messages will always be displayed!
_NONE_ = 0
_INFO_ = 1
_ALL_  = 5
WARNING = '\033[93m'
FAIL    = '\033[91m'
BLUE    = '\033[1;35m'
ENDC    = '\033[0m'
logLevel =  _NONE_ #_ALL_ #_NONE_, _ALL_

def __logError__(msg):
    __log__(FAIL, "ERROR", msg)
def __logInfo__(msg):
    if (logLevel >= _INFO_):
        __log__(BLUE, "INFO ", msg)
def __logDebug__(msg):
    if (logLevel >= _ALL_):
        __log__(WARNING,"DEBUG", msg)
def __log__(color, level, msg):
    currDay = datetime.datetime.now().strftime('%m-%d-%Y')
    currTime = datetime.datetime.now().strftime('%H:%M:%S')
    print "{}{} - {} - {} - {}{}".format(color, currDay, currTime, level, msg, ENDC)



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
        return self.load_view('index.html')

    def process(self):
        __logDebug__("Entering process()...")
        __logError__("Problem")

        __logDebug__("Invoke redirect('/')")
        return redirect('/')
