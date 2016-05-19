from system.core.controller import *
import logging
import re
from flask import flash

class Users(Controller):

    def __init__(self, action):
        logging.debug("init:begin")
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db

    def index(self):
        logging.debug("index:begin")

        if 'id' in session: # id in session obj, get user data now

            user = self.models['User'].getUserById(session['id'])
            return self.load_view('success.html', user = user)

        else:  # id not in session, prompt user for email and auth
            logging.warning("id not in session object")
            return self.load_view('index.html') # show login form

    def process_login(self):
        """ handle the login: perform user validation """
        # query results
        qr = self.models['User'].login_user(request.form)

        if qr['status'] == True:
            session['id'] = qr['user']['id']
            return self.load_view('success.html', user = qr['user'])
        for message in qr['errors']:
            logging.debug(message)
            flash(message)
            return redirect('/')

    def logout(self):
        """ remove id from session to log user out of application """
        session.clear()
        return redirect('/')

    def process_registration(self):
        """ handle the login """

        info = {
            'first_name': request.form['fn'],
            'last_name': request.form['ln'],
            'email': request.form['email'],
            'password':request.form['password'],
            'cpassword': request.form['cpassword']
        }
        qr = self.models['User'].create_new(info)

        # failed to add user to db
        if qr['status'] == False:
            for message in qr['errors']:
                flash(message)
            return redirect('/register')

        # added user okay
        qr = self.models['User'].getUserById(qr['user'])
        return self.load_view('success.html', user = qr['user'])

    def register(self):
        return self.load_view('registration.html')
