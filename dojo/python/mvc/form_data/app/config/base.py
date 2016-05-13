"""
    Base Configuration File
"""
""" Put Generic Configurations here """
import datetime


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'someSecretKey'

""" Put Development Specific Configurations here """
class DevelopmentConfig(Config):
    DEBUG = True

    # Logging Utilities
    # Guy Whorley
    # Using ANSII Colors to print color console messages
    # To enable various levels of log messages, set logLevel as follows:
    #   logLevel = _NONE_ | _INFO_ | _ALL_
    #   NOTE: Error messages will always be displayed!

    _NONE_ = 0
    _INFO_ = 1
    _ALL_  = 5
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    BLUE    = '\033[1;35m'
    ENDC    = '\033[0m'
    logLevel = _INFO_

    def __logError__(self, msg):
        __log__(self, FAIL, "ERROR", msg)
    def __logInfo__(self, msg):
        if (logLevel == _INFO_):
            __log__(self, BLUE, "INFO ", msg)
    def __logDebug__(self, msg):
        if (logLevel == _ALL_):
            __log__(self, WARNING,"DEBUG", msg)
    def __log__(self, color, level, msg):
        currDay = datetime.datetime.now().strftime('%m-%d-%Y')
        currTime = datetime.datetime.now().strftime('%H:%M:%S')
        print "{}{} - {} - {} - {}{}".format(color, currDay, currTime, level, msg, ENDC)

""" Put Staging Specific Configurations here """
class StagingConfig(Config):
    TESTING = True

""" Put Production Specific Configurations here """
class ProductionConfig(Config):
    pass
