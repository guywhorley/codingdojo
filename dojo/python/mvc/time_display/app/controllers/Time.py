"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import datetime

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        # comment in IF you have a model for Test...   self.load_model('TestModel')
        self.db = self._app.db
        """
        This is an example of a controller method that will load a view for the client
        """

    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """

        currDay = datetime.datetime.now().strftime('%b %d, %Y')
        currTime = datetime.datetime.now().strftime('%H:%M %p')

        # print "*"*20
        # print currDay
        # print currTime
        # print "*"*20

        return self.load_view('Time/index.html', day = currDay, time = currTime )

    def hello(self):
        return "Hello World"
