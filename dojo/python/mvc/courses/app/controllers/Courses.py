from system.core.controller import *
import logging
import datetime
import re

class Courses(Controller):

    def __init__(self, action):
        logging.debug("init:begin")
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        # logging.debug("index:begin")

        # testing the model
        # course = {
        #     'title':'Scrum in a Day',
        #     'description': 'Fundamentals of Agile/Scrum',
        # }
        #messages = self.models['Course'].add_course(course)
        # messages = self.models['Course'].get_courses()
        # messages = self.models['Course'].delete_courseById(4)
        # logging.info(messages)


        """
        A loaded model is accessible through the models attribute
        self.models['CoursesModel'].get_users()

        self.models['CoursesModel'].add_message()
        # messages = self.models['CoursesModel'].grab_messages()
        # user = self.models['CoursesModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        # Get Course Listing
        courses = self.models['Course'].get_courses()
        logging.debug(courses)

        # logging.debug("index:end")
        return self.load_view('index.html', courses = courses)

    def confirm_delete(self, course_id):
        """ Prompt user for final delete confirmation """
        logging.warning("id: {}".format(course_id))
        course = self.models['Course'].get_courseById(course_id)
        return self.load_view('confirmdelete.html', course = course)

    def destroy(self, course_id):
        """ Remove a course from the course catalog """
        logging.debug("destroying course:{}".format(course_id))
        self.models['Course'].delete_courseById(course_id)
        return redirect('/')

    def add_course(self):
        """ Add a course to the course catalog """
        # logging.debug("adding course...")

        # Get and Validate Form Data
        REGEX_TITLE = re.compile('^\w.{14,120}$')
        REGEX_DESC = re.compile('^\w.{1,255}$')
        matchTitle = False
        # matchDesc = False
        title = None
        desc = None

        if REGEX_TITLE.match(request.form['title']):
            matchTitle = True
            title = request.form['title'].strip()
        #if REGEX_DESC.match(request.form['description']):
        #    matchDesc = True
        desc = request.form['description'].strip()

        if (matchTitle): #and matchDesc):
            # create course dict and call model
            course = {
                'title': request.form['title'],
                'description': request.form['description']
            }
            self.models['Course'].add_course(course)
        else:
            logging.warning("Validation failed! title={} desc={}".format(title, desc))

        return redirect('/')
