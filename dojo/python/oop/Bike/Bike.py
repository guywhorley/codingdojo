class Bike(object):
    """
    The Bike class represents non-motorized, land-traveling, single-occupancy
     vehicles.
    """
    def __str__(self):
        return "[Class:Bike, Price:{}, Max-Speed:{}, Total-Miles:{}]".format(self.price, self.max_speed,self.miles)

    def __init__(self, price=0, max_speed=12):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        """ Display price, max speed, total miles for this bike. """
        return self.__str__()

    def ride(self):
        """ Display 'Riding' and add 10 to self.miles """
        self.miles += 10
        print "Riding 10 miles."
        return self

    def reverse(self):
        """ Display 'Reversing' and decrease total miles by 5 """
        if self.miles <= 0:
            self.miles = 0
            print "You tried pedaling backwards in space/time."
        else:
            self.miles -= 5
            print "Reversing 5 miles. "
        return self

# Class tester
b1 = Bike(100, 12)
print "Bike1 initial state: {}".format(b1.displayInfo())
b1.reverse().reverse()
b1.ride().ride().ride().reverse()
print "Bike 1 ending state:{}".format(b1.displayInfo())
