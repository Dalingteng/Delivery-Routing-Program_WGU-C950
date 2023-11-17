# Create Package class
class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zipcode,
                                                       self.deadline, self.weight, self.delivery_time, self.status)

    def updateStatus(self, input_time):
        if self.delivery_time < input_time:
            self.status = "Delivered"
        elif self.departure_time > input_time:
            self.status = "En route"
        else:
            self.status = "At the hub"
    