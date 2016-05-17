from underscore import *
import pytest

class TestUnderscore(object):

    # setup any req'd data here
    def setup(self):
        self.intArr = [-2,5,1,90,23,-23,101]
        self.mapArr = [ 0,7,3,92,25,-21,103]
        self.strAttr = ['Bob', 'Chris', 'Christina','Rachel', 'Moka']

    def test_map(self):
        _ = Underscore()
        assert _.map(self.intArr, lambda x: x+2) == self.mapArr

    def test_reduce(self):
        _ = Underscore()
        assert _.reduce(self.intArr, lambda x: x,5) == 200


    def test_find_valueExists(self):
        _ = Underscore()
        assert _.find(self.strAttr, lambda x: x=='Moka') == 'Moka'

    def test_find_valueDoesNotExist(self):
        _ = Underscore()
        assert _.find(self.strAttr, lambda x: x=='Jared') == None


    def test_filter(self):
        _ = Underscore()
        assert _.filter(self.intArr, lambda x: x%2==1) == [5,1,23,-23,101]

    def test_reject(self):
        _ = Underscore()
        assert _.reject(self.intArr, lambda x: x<70) == [90,101]
