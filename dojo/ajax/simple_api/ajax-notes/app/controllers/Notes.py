from system.core.controller import *
import logging
#import re
#from flask import flash

class Posts(Controller):

    def __init__(self, action):
        logging.debug("init:begin")
        super(Posts, self).__init__(action)

        self.load_model('Post')
        self.db = self._app.db

    def index(self):
        posts = self.models['Post'].all()
        return self.load_view('posts/index.html', posts=posts)

    def index_json(self):
        """ Get posts in json format """
        posts = self.models['Post'].all()
        return jsonify(posts=posts)

    def index_html(self):
        """ Get posts as html partial """
        posts = self.models['Post'].all()
        return self.load_view('partials/posts.html', posts=posts)

    def create(self):
        """ create a new post """
        logging.error('create new post')
        new_post = { "message":  request.form['post'] }
        self.models['Post'].create(new_post)
        posts = self.models['Post'].all()
        return self.load_view('partials/posts.html', posts=posts)
