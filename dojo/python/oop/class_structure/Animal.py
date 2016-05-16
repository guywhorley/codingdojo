"""
The Animal class represents the basic states and behavior of animals in general.
"""
class Animal(object):

    def __init__(self,
                description='A generic animal',
                color='basic black',
                category='living',
                age=0,
                name="whatzit"):
        ''' Initialize your Animal '''
        self.description = description
        self.color = color
        self.category = category
        self.age = age
        self.name = name

    def move(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

    def __str__(self):
        return "['name':'{}'', 'category':'{}'', 'color':'{}', 'age':{}, 'description':'{}']".format(self.name, self.category, self.color, str(self.age), self.description)

Moka = Animal("My good dog", "black", "dog", 3, "Moka")
print "My pet, {}, is a good {}!".format(Moka.name, Moka.category)
print Moka
