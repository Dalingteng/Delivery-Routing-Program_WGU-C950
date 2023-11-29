from datetime import timedelta


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
        self.departureTime = timedelta()
        self.deliveryTime = timedelta()
        self.truckNumber = None

    def __str__(self):
        if self.status == "IN HUB":
            self.status = self.status
        elif self.status == "Delivered":
            self.status = self.status + " at " + str(self.deliveryTime)
        elif self.status == "En route":
            self.status = self.status + " - Truck " + str(self.truckNumber)
        return ("%s | %s | %s | %s | %s | %s | %s kg | %s" %
                (self.id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status))

    # Function to update status of package upon a specific time
    def updateStatus(self, input_time):
        if input_time < self.departureTime:
            self.status = "IN HUB"
        elif input_time < self.deliveryTime:
            self.status = "En route"
        else:
            self.status = "Delivered"
        # Update address of package 9 at 10:20
        if self.id == 9:
            if input_time > timedelta(hours=10, minutes=20):
                self.address = "410 S State St"
                self.zipcode = "84111"
            else:
                self.address = "300 State St"
                self.zipcode = "84103"
