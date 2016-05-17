"""
    System Initialization File

    Loads initializers for configurations, database, and routes and creates the flask application
"""
from flask import Flask
import os
from app.config import routes

from system.init.configuration import initialize_config
from system.init.database import initialize_db
from system.init.routes import initialize_routes
import logging

# LOGGING FOR CONTROLLERS AND MODELS
# Ensure that each ontroller and model class have: 'import logging'

# GLOBAL LOG LEVEL: uncomment the desired global log level
# Initialize Logging Variables
# logLevel = logging.NOTSET
# logLevel = logging.ERROR
logLevel = logging.DEBUG
# logLevel = logging.INFO

# LOG FILE FORMAT AND FILE-NAME
logFormat = '%(asctime)s   %(levelname)-7s {%(filename)s#%(funcName)s}\tLn:%(lineno)-3d - %(message)s'
logFile = './logs/controller-surveys.log'
logging.basicConfig(format=logFormat, filename=logFile, level=logLevel)


def initialize_app():

    instance_path = os.path.abspath(os.path.dirname(__file__) + '/../..')
    template_folder = os.path.join(instance_path, 'app/views')
    static_folder = os.path.join(instance_path, 'app/static')

    app = Flask('app', static_folder=static_folder, template_folder=template_folder, instance_path=instance_path)

    initialize_config(app)
    initialize_db(app)
    initialize_routes(app)

    return app
