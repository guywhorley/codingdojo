"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import logging

class Course(Model):
    def __init__(self):
        logging.debug("Course-init:begin")
        super(Course, self).__init__()

    # CREATE courses - validated!
    def add_course(self, course ):
        """ Add course. 'course' param is dictionary with key/val pairs """
        logging.debug("add_course:begin")
        query = "INSERT INTO courses (title, description, created_at, updated_at) VALUES(:title, :description, NOW(), NOW())"
        data = {
            'title':course['title'],
            'description':course['description'],
            }
        return self.db.query_db(query, data)

    # READ courses - validated!
    def get_courses(self):
        """ Get all courses """
        logging.debug("f(x) entry")
        query = "SELECT * from codingdojo.courses ORDER BY title ASC"
        return self.db.query_db(query)

    # DELETE courses - validated
    def delete_courseById(self, course_id):
        """ Delete course by course_id """
        logging.debug("delete course by id:{}".format(course_id))
        query = "DELETE FROM courses WHERE id = :id"
        data  = { 'id': course_id }
        return self.db.query_db(query, data)

    """
    Below is an example of a model method that queries the database for all users in a fictitious application

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
