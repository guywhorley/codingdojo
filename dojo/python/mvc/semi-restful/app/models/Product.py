
from system.core.model import Model
import logging
import re

class Product(Model):

    """ bcrypt & mySQL: pw_hash column - ensure that the type is varchar(255) """

    def __init__(self):
        logging.debug("init_model:begin")
        super(Product, self).__init__()


    def create(self):
        logging.debug("model: create()")

    def read_one(self):
        logging.debug("model: read_one()")

    def read_all(self):
        logging.debug("model: read_all()")

    def update(self):
        logging.debug("model: update()")

    def delete(self):
        logging.debug("model: delete()")



    # def create_new(self, info):
    #     """ Add user to users table """
    #     logging.debug("creating new user: {} {}".format(info['first_name'], info['last_name']))
    #
    #     # Using code from jihyechoing for validation
    #     # Validate in the model, not the controller
    #     EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
    #
    #     # keep track of errors
    #     # Errors accumulate here but are displayed in controller via flash messages
    #     # in jinja2 template on html pages
    #     errors = []
    #
    #     if len(info['first_name']) < 2 or len(info['last_name']) < 2:
    #         errors.append('First and Last Name must be at least 2 characters long')
    #     elif not info['email']:
    #         errors.append('Email cannot be blank')
    #     elif not EMAIL_REGEX.match(info['email']):
    #         errors.append('Email format must be valid!')
    #     elif not info['password']:
    #         errors.append('Password cannot be blank')
    #     elif len(info['password']) < 8:
    #         errors.append('Password must be at least 8 characters long')
    #     elif info['password'] != info['cpassword']:
    #         errors.append('Password and confirmation must match!')
    #
    #     if errors: # errors are present
    #         # use a dictionary to return multiple return values from the call
    #         return { 'status': False, 'errors': errors }
    #     else:
    #         password = info['password']
    #         hashed_pw = self.bcrypt.generate_password_hash(password)
    #         query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:fn, :ln, :email, :pw, NOW(), NOW())"
    #         data = {
    #             'fn': info['first_name'],
    #             'ln': info['last_name'],
    #             'email': info['email'],
    #             'pw': hashed_pw
    #         }
    #         # the INSERT query returns the id of the record that was created
    #         user = self.db.query_db(query, data)
    #         logging.warning("createdUser: {}".format(user))
    #         return { 'status': True, 'user': user }
    #
    # def getUserById(self, id):
    #     """ Query users table for user id """
    #     logging.info("get user by id: {}".format(id))
    #     errors = [] # setup list to hold error messages
    #
    #     query = "SELECT * FROM users WHERE id = :id LIMIT 1"
    #     data = { 'id': id }
    #     user = self.db.query_db(query, data)
    #
    #     if not user:
    #         errors.append("User id was not found!")
    #         return { "status": False, 'errors': errors }
    #     # return just the first record in the query result
    #     return { "status": True, "user": user[0] }
    #
    # def login_user(self, info):
    #     """ Query users table for user by email. If exists, check passwords match. If so, return True """
    #     logging.info("logging in user: {}".format(info['email']))
    #     errors = [] # setup a list to hold error messages
    #
    #     password = info['password']
    #     query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    #     data = { 'email': info['email'] }
    #
    #     user = self.db.query_db(query, data)
    #
    #     if not user: # user was not found
    #         errors.append("I don't recognize the email {}.".format(info['email']))
    #         return { 'status': False, 'errors': errors }
    #     else:
    #         # work with failure case first for quick return
    #         if not self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
    #             errors.append("Incorrect password.")
    #             return { 'status': False, 'errors': errors }
    #         else:
    #             return { 'status': True, 'user': user[0] }
