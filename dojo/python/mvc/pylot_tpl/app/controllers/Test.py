"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from gutils.glog import *

class Test(Controller):

    def __init__(self, action):
        logging.debug('init:begin')
        super(Test, self).__init__(action)

        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """

        # comment in IF you have a model for Test...   self.load_model('TestModel')
        self.db = self._app.db
        """
        This is an example of a controller method that will load a view for the client
        """

    def index(self, name, id):
        # logging.debug("index:begin")

        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        # logging.debug("index:end")
        return self.load_view('Test/index.html', name = name, id = id)

    def admin(self, name, id='007'):
        # logging.debug("admin:begin")

        # logging.debug("admin:end")
        return "<h1>Test#admin</h1><p>Hello {}. Your ID is {}.</p><p>You have reached the admin page for 'Test'.</p>".format(name, id)
