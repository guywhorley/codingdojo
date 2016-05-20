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

        products = self.models['Product'].read_all()

        if products['status'] == False:
            return self.load_view('index.html', products = "")
        return self.load_view('index.html', products = products['data'])

    def new(self):
        """ Create new product """
        logging.debug("enter launch_create()")
        return self.load_view('add.html')

    def edit(self, id):
        """ Edit existing product """
        logging.debug("enter edit()")

        products = self.models['Product'].read_one(id)
        return self.load_view("edit.html", item = products['data'])

    def show(self, id):
        """ Show product details """
        logging.debug("enter show()")

        products = self.models['Product'].read_one(id)
        return self.load_view("show.html", item = products['data'])

    def process_create(self):
        """ Create new product """
        logging.debug("enter create()")
        if request.form:
            errors = []
            records = self.models['Product'].create(request.form)
            if records['status'] == False:
                errors.append("I was not able to add the new product!")
                return redirect('/launch_create', messages = errors)
            return redirect('/')
        else:
            return self.load_view('launch_create.html')

    def destroy(self):
        """ Delete product """
        logging.debug("enter destroy()")
        if request.form['product-id']:
            records = self.models['Product'].delete(request.form['product-id'])
        return redirect('/')

    # NOTE: cannot redirect to a form using args, must use load_view instead

    def update(self):
        """ Update product """
        logging.debug("enter update()")
        records = self.models['Product'].update(request.form)
        if not records['status']:
            return self.load_view('/', messages = records['errors'])
        return redirect('/')
