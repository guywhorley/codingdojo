from system.core.controller import *
import logging

class Courses(Controller):

    def __init__(self, action):
        logging.debug("init:begin")
        super(Courses, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        # logging.debug("index:begin")

        # testing the model
        course = {
            'title':'Scrum in a Day',
            'description': 'Fundamentals of Agile/Scrum',
        }
        messages = self.models['Course'].add_course(course)

        # messages = self.models['Course'].get_courses()
        # messages = self.models['Course'].delete_courseById(4)
        logging.info(messages)


        """
        A loaded model is accessible through the models attribute
        self.models['CoursesModel'].get_users()

        self.models['CoursesModel'].add_message()
        # messages = self.models['CoursesModel'].grab_messages()
        # user = self.models['CoursesModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """

        # logging.debug("index:end")
        return self.load_view('index.html')
