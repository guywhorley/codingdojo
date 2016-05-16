# Logging Functions
# Author: Guy Whorley
# Description: Colorized console messages at different log levels.
#   Global log level is indicated by 'logLevel' flag set to  _NONE_,
#   _INFO_, or _ALL_. Custom error messages will always be printed to
#   the console. To enable various levels of log messages, set logLevel
#   as follows: logLevel = _NONE_ | _INFO_ | _ALL_

import datetime

_NONE_ = 0
_INFO_ = 1
_ALL_  = 5
WARNING = '\033[93m'
FAIL    = '\033[91m'
BLUE    = '\033[1;35m'
ENDC    = '\033[0m'
logLevel =  _ALL_ #_NONE_, _ALL_

def glogError(msg):
    __log__(FAIL, "ERROR", msg)
def glogInfo(msg):
    if (logLevel >= _INFO_):
        __log__(BLUE, "INFO ", msg)
def glogDebug(msg):
    if (logLevel >= _ALL_):
        __log__(WARNING,"DEBUG", msg)
def __log__(color, level, msg):
    currDay = datetime.datetime.now().strftime('%m-%d-%Y')
    currTime = datetime.datetime.now().strftime('%H:%M:%S')
    print "{}{} - {} - {} - {}{}".format(color, currDay, currTime, level, msg, ENDC)
