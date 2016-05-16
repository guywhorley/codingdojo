import logging
"""
Use Pyhon's logging modules for my controllers.
To use:
    0. To set global log level, edit /controllers/gutils.glog.py and set logLevel to desired level, save file.
    1. Ensure that the gtils module is present in the /controllers and /models directories.
    2. Ensure that 'from gutils.glog import *' is placed at top of .py file.
    3. Put logging messages as follows:
        logging.info('<msg>')  | .error, .warning, .debug
"""

# logLevel = logging.NOTSET
# logLevel = logging.ERROR
logLevel = logging.DEBUG
# logLevel = logging.INFO

# Initialize Logging Variables
logFormat = '%(asctime)s   %(levelname)-7s {%(filename)s#%(funcName)s}\tLn:%(lineno)-3d - %(message)s'
logFile = './logs/controller-surveys.log'
logging.basicConfig(format=logFormat, filename=logFile, level=logLevel)
