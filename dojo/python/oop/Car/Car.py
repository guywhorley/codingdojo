class Car(object):
    """ The Car class represents motorized vehicles. """

    def __init__(self,
                 price = 0,
                 speed = 0,
                 fuel = "Empty",
                 mileage = 20):
        """Default Car class: price,speed = 0; mileage = 20; fuel = 'Empty'"""
        if price < 0:
            self.price = 0
            self.tax = 0.12
        elif price > 10000:
            self.price = price
            self.tax = 0.15
        else:
            self.price = price
            self.tax = 0.12

        if speed < 0:
            speed = 0
        self.speed = speed

        self.fuel = fuel

        if mileage < 0:
            mileage = 20
        self.mileage = mileage

    def display_all(self):
        """ Display this car's attributes."""
        print "Price:{}\nSpeed:{}mph\nFuel:{}\nMileage:{}mpg\nTax:{}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

# end Car Class

c1 = Car(2000, 35, "Full", 15)
c1.display_all()
print "\n"

c2 = Car(2000, 5, "Not Full", 105)
c2.display_all()
print "\n"

c3 = Car(2000, 15, "Kind of Full", 95)
c3.display_all()
print "\n"

c4 = Car(2000, 45, "Empty", 25)
c4.display_all()
print "\n"

c5 = Car(200000, 35, "Empty", 15)
c5.display_all()
