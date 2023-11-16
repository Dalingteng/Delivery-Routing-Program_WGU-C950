# Create Truck class
class Truck:
    def __init__(self, capacity, speed, load, package, mileage, address, departure_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.package = package
        self.mileage = mileage
        self.address = address
        self.departure_time = departure_time
        self.time = departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.package,
                                               self.mileage, self.address, self.departure_time)