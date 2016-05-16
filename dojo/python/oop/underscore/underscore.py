# filename: underscore.py
# author: guy whorley

class Underscore(object):
    """ Underscore library """

    def map(self): pass

    def reduce(self): pass

    def find(self): pass

    def filter(self, myLambda,*args):
        temp = []
        temp.append(mylamda, *args)
        return temp

    def reject(self): pass

# tester
args = ["x","x%2==0"]
_ = Underscore()
num = [1,2,3,4]

f = lambda x: x%2==0
_.filter(f, *args)
