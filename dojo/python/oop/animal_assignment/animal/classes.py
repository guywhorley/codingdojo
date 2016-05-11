# filename: classes.py
# author: guy whorley
# description: class definitions for animal, dog, dragon

class Animal(object):
    """ This class represents the basic animal and is the base class for all other animals."""

    def __init__(self,
                 name='nonce'):
        """ Defaults: name=nonce """
        self.name = name
        self.health = 100

    def __dropHealth__(self, mode, n):
        if (self.health >= n):
            self.health -= n
        else:
            print "Animal doesn't have enough health to {} [required:{} available:{}]!".format(mode, n, self.health)

    def walk(self):
        """ Animal walks and loses 1 pt health """
        print "{} is walking...".format(self.name)
        self.__dropHealth__("walk", 1)
        return self

    def run(self):
        """ Animal runs and loses 5 pts health """
        print "{} is running...".format(self.name)
        self.__dropHealth__("run", 5)
        return self

    def displayHealth(self):
        """ Show health stats of animal """
        print "name:{}, health:{}".format(self.name, self.health)
        return self

# Tester
animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()
