
from system.core.model import Model
import logging
import re
import datetime

class Quote(Model):
    """
    bcrypt & mySQL: pw_hash column - ensure that the type is varchar(255)
    """

    def __init__(self):
        super(Quote, self).__init__()

    def add_favorite_quote(self, id, q_id):
        """ add quote with q_id to favorite's list for user:id """
        query = "INSERT INTO favorites (user_id, quote_id, created_at, updated_at) VALUES (:id, :quote_id, NOW(), NOW())"
        data = {
            'id' : id,
            'quote_id' : q_id
        }
        self.db.query_db(query, data)
        return { 'status':True, 'data': [] }

    def remove_favorite_quote(self, id, q_id):
        """ remove quote with q_id from favorite's list for user:id """
        query = "DELETE FROM favorites WHERE user_id = :id AND quote_id = :q_id"
        data = {
            'id' : id,
            'q_id' : q_id
        }
        self.db.query_db(query, data)
        return { 'status': True, 'data': [] }

    def get_quotes_posted_by_user(self, id):
        errors =[]

        query = "SELECT * FROM quotes q WHERE  q.posted_by = :id"
        data = { 'id' : id }
        qr = self.db.query_db(query, data)

        if not qr:
            errors.append("Problem retrieving quotes for user {}".format(id))
            return { 'status' : False, 'errors' : errors }
        return { 'status': True, 'count': len(qr), 'data': qr }

    def add_quote(self, id, form):
        errors = []
        if len(form['author']) < 3:
            errors.append('Author name must be three or more characters long')
        elif len(form['quote']) < 10:
            errors.append('Message must be ten or more characters long')

        if errors:
            return { 'status': False, 'errors': errors }
        else:
            # logging.warning("{}::{}::{}".format(id, form['author'], form['quote']))
            query = "INSERT INTO quotes (quote, author, posted_by, created_at, updated_at) VALUES (:quote, :author, :posted_by, NOW(), NOW())"
            data = {
                'quote': form['quote'],
                'author' : form['author'],
                'posted_by' : id
            }
            # the INSERT query returns the id of the record that was created
            quote = self.db.query_db(query, data)
            logging.warning("createdUser: {}".format(quote))
            return { 'status': True, 'user': quote }

    def login_user(self, form):
        errors = []

        password = form['password']
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': form['email'] }

        user = self.db.query_db(query, data)

        if not user:
            errors.append("I don't recognize the email {}.".format(form['email']))
            return { 'status': False, 'errors': errors }
        else:
            # work with failure case first for quick return
            if not self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                errors.append("Incorrect password.")
                return { 'status': False, 'errors': errors }
            else:
                return { 'status': True, 'user': user[0] }

    def getUserById(self, id):
        errors = []

        query = "SELECT * FROM users WHERE id = :id LIMIT 1"
        data = { 'id': id }
        user = self.db.query_db(query, data)

        logging.warning('user info: {}'.format(user))

        if not user:
            errors.append("User id was not found!")
            return { "status": False, 'errors': errors }
        # return just the first record in the query result
        return { "status": True, "user": user[0] }

    def get_all_quotes(self):
        errors = []

        query = "SELECT * FROM quotes"
        data = {}
        records = self.db.query_db(query, data)
        logging.warning(records)

        if not records:
            errors.append("Problem retrieving quotes!?")
            return { 'status' : False, 'errors' : errors }
        return { 'status': True, 'data': records }

    def get_all_non_favorite_quotes(self, id):
        errors = []

        # query = "SELECT quotes.posted_by, quotes.id, quotes.quote, quotes.author, users.alias FROM quotes q LEFT OUTER JOIN favorites f ON q.id = f.quote_id LEFT JOIN users ON users.id = favorites.user_id where favorites.id IS NULL or favorites.user_id = :id"
        query = "SELECT q.posted_by, q.id, q.quote, q.author, u.alias from quotes q LEFT OUTER JOIN favorites f ON q.id = f.quote_id LEFT JOIN users u ON f.user_id = u.id WHERE f.user_id IS NULL OR f.user_id != :id"
        data = { 'id' : id  }

        records = self.db.query_db(query, data)
        # logging.warning(records)

        if not records:
            return { 'status' : True, 'data' : [] }
        return { 'status': True, 'data': records }

    def get_all_favorite_quotes(self, id):

        query = "SELECT * FROM quotes JOIN favorites ON quotes.id = favorites.quote_id JOIN users ON users.id = favorites.user_id WHERE users.id = :id"
        data = { 'id' : id }
        records = self.db.query_db(query, data)
        logging.warning(records)

        if not records:
            return { 'status' : True, 'data' : [] }
        return { 'status': True, 'data': records }

    def login_user(self, info):
        errors = []

        password = info['password']
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': info['email'] }

        user = self.db.query_db(query, data)

        if not user:
            errors.append("I don't recognize the email {}.".format(info['email']))
            return { 'status': False, 'errors': errors }
        else:
            # work with failure case first for quick return
            if not self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                errors.append("Incorrect password.")
                return { 'status': False, 'errors': errors }
            else:
                return { 'status': True, 'user': user[0] }

    def getUserById(self, id):
        errors = []

        query = "SELECT * FROM users WHERE id = :id LIMIT 1"
        data = { 'id': id }
        user = self.db.query_db(query, data)

        if not user:
            errors.append("User id was not found!")
            return { "status": False, 'errors': errors }
        # return just the first record in the query result
        return { "status": True, "user": user[0] }

    def create_new(self, form):
        """ Add user to users table """
        errors = []
        if len(form['name']) < 2:
            errors.append('First and Last Name must be at least 2 characters long')
        elif not form['alias']:
            errors.append('Alias cannot be blank')
        elif not form['email']:
            errors.append('Email cannot be blank')
        #elif not EMAIL_REGEX.match(info['email']):
        #    errors.append('Email format must be valid!')
        elif not form['password']:
            errors.append('Password cannot be blank')
        elif not form['dob']:
            errors.append('Date-of-birth cannot be blank')
        elif len(form['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif form['password'] != form['cpassword']:
            errors.append('Password and confirmation must match!')

        if errors:
            return { 'status': False, 'errors': errors }
        else:
            password = form['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = "INSERT INTO users (name, alias, email, pw_hash, dob, created_at, updated_at) VALUES (:name, :alias, :email, :pw, :dob, NOW(), NOW())"

            my_dob = datetime.datetime.strptime(form['dob'], '%Y-%m-%d').date()

            data = {
                'name': form['name'],
                'alias' : form['alias'],
                'email': form['email'],
                'pw': hashed_pw,
                'dob' : my_dob
            }

            # the INSERT query returns the id of the record that was created
            user = self.db.query_db(query, data)
            logging.warning("createdUser: {}".format(user))
            return { 'status': True, 'user': user }
