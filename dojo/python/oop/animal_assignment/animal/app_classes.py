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
        msg= "name:{}, health:{}".format(self.name, self.health)
        return msg

class Dog(Animal):
    """ This class represents our four-legged friends """

    def __init__(self,
                 name = "nonce"):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        print "Petting {}...".format(self.name)
        return self

class Dragon(Animal):
    """ Ths class represents misunderstood gentle, fire-breathing reptiles """

    def __init__(self,
                 name = "nonce"):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        print "{} is flying...".format(self.name)
        self.__dropHealth__("fly",10)
        return self

    def displayHealth(self):
        return "This is a dragon! " + super(Dragon, self).displayHealth()
