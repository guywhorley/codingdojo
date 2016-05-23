from system.core.controller import *
import logging

class Quotes(Controller):

    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('Quote')
        self.db = self._app.db

    def index(self):
        if 'id' not in session:
            return self.load_view('login-regis.html')

        all_quotes = self.models['Quote'].get_all_non_favorite_quotes(session['id'])
        all_favs = self.models['Quote'].get_all_favorite_quotes(session['id'])

        return self.load_view('index.html/', all_quotes = all_quotes['data'], all_favs = all_favs['data'] )

    def show_user_details(self, id):
        poster = self.models['Quote'].getUserById(id);

        qr = self.models['Quote'].get_quotes_posted_by_user(id)

        if qr['status'] == True:
            return self.load_view('show.html', poster = poster['user'], posts = qr['data'], count = qr['count'])

        for message in qr['errors']:
            flash(message)
            return self.load_view('show.html', poster = poster['user'], posts = [], count = 0)

    def add_favorite_quote(self, id, q_id):
        qr = self.models['Quote'].add_favorite_quote(id, q_id )
        return redirect('/')

    def remove_favorite_quote(self, id, q_id):
        qr = self.models['Quote'].remove_favorite_quote(id, q_id )
        return redirect('/')

    def process_add_quote(self):
        qr = self.models['Quote'].add_quote(session['id'], request.form)
        return redirect('/')

    def process_login(self):
        qr = self.models['Quote'].login_user(request.form)

        if qr['status'] == True:
            session['id'] = qr['user']['id']
            session['username'] = qr['user']['name']
            session['useralias'] = qr['user']['alias']
            return redirect('/')
        for message in qr['errors']:
            logging.debug(message)
            flash(message)
            return self.load_view('login-regis.html')

    def logout(self):
        session.clear()
        return redirect('/')

    def process_registration(self):
        qr = self.models['Quote'].create_new(request.form)

        if qr['status'] == False:
            for message in qr['errors']:
                flash(message)
            return redirect('/')

        qr = self.models['Quote'].getUserById(qr['user'])

        session['id'] = qr['user']['id']
        session['useralias'] = qr['user']['alias']
        # logging.error("user id is: {}".format(qr['user']['id']))
        return redirect('/')

    # NOTE: cannot redirect to a form using args, must use load_view instead
