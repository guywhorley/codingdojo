# filename: math_dojo.py
# author: guy whorley

from types import *


class MathDojo(object):
    """ This class represents a simple set of mathematical functions. """

    def __init__(self):
        """ Comments Here """
        self.result = 0

    def add(self, *args):
        """ Add args together, then add to results. numbers together """
        if not  args:
            return self
        for curr in args:
			if type(curr) is list:
				self.add(*curr)
			elif type(curr) is dict:
				self.add(**curr)
			else:
				self.result += curr
        return self;


    def subtract(self, *args):
        """ Add args together, then subtract from result. Ignore if empty args. """
        temp = 0
        if not args:
            return self
        for curr in args:
            if type(curr) is list:
                self.subtract(*curr) # recurse over list
            elif type(curr) is dict:
                self.subtract(**curr) # recurse over dict
            else:
                self.result -= curr
        return self
