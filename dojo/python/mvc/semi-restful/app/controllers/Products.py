from system.core.controller import *
import logging
#import re
#from flask import flash

class Products(Controller):

    def __init__(self, action):
        logging.debug("init:begin")
        super(Products, self).__init__(action)

        self.load_model('Product')
        self.db = self._app.db

    def index(self):
        """ Show index page """
        logging.debug("enter index()")
        return self.load_view('index.html')

    def new(self):
        """ Create new product """
        logging.debug("enter new()")

    def edit(self):
        """ Edit existing product """
        logging.debug("enter edit()")

    def show(self):
        """ Show product details """
        logging.debug("enter show()")

    def create(self):
        """ Create new product """
        logging.debug("enter create()")

    def destroy(self):
        """ Delete product """
        logging.debug("enter destroy()")

    def update(self):
        """ Update product """
        logging.debug("enter update()")

            
