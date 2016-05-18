"""
    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Note: bcrypt and your db pw_hash column - ensure that the type is varchar(255)

"""
from system.core.model import Model
import logging

class WelcomeModel(Model):
    def __init__(self):
        logging.debug("init_model:begin")
        super(WelcomeModel, self).__init__()

    def create_new(self, info):
        logging.debug("creating new user")
        password = info['password']
        hashed_pw = self.bcrypt.generate_password_hash(password)
        query = "INSERT INTO users (first_name, last_name, pw_hash, created_at) VALUES (:first_name, :last_name, :pw_hash, NOW()"
        data = {
            'first_name': info['first_name'],
            'last_name': info['last_name'],
            'pw_hash'] = hashed_pw
        }
        self.db.query_db(query, data)

    def login_user(self, info):
        logging.debug("logging in user")
        password = info['password']
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': info['email'] }
        user = self.db.query_db(query, data).fetchone()
        # valid user email
        if user:
            # compare encr pw in db to one provided by user
            if self.bcrypt.check_password_hash(user.pw_hash, password):
                return user
        return False
        
    """
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True

    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)
    """
