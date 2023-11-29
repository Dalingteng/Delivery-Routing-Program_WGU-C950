# Author: Sochandaling Teng
# Student ID: 010309126

import csv
from datetime import timedelta
from hashtable import HashTable
from package import Package
from truck import Truck
from builtins import ValueError

# Load and read the csv files
with open("csv/package.csv") as packageCSV:
    PackageCSV = csv.reader(packageCSV)
    PackageCSV = list(PackageCSV)
with open("csv/distance.csv") as distanceCSV:
    DistanceCSV = csv.reader(distanceCSV)
    DistanceCSV = list(DistanceCSV)
with open("csv/address.csv") as addressCSV:
    AddressCSV = csv.reader(addressCSV)
    AddressCSV = list(AddressCSV)


# Function to load packages from package csv file into the hash table
def loadPackageData(filename):
    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "IN HUB"
            # Create package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)
            # Insert package object into the hash table
            packageHashTable.insert(pID, p)


# Create a hash table for packages
packageHashTable = HashTable()


# Load packages from package csv file into the hash table
loadPackageData('csv/package.csv')


# Function to find distance between two addresses
def distanceBetween(address1, address2):
    distance = DistanceCSV[address1][address2]
    if distance == '':
        distance = DistanceCSV[address2][address1]
    return float(distance)


# Function to find index of address from address csv file
def address(a):
    for row in AddressCSV:
        if a in row[2]:
            return int(row[0])


# Create truck objects and manually load the trucks based on criteria
# Truck 1 packages: deadline by 10:30 except 6 & 25 delayed, 15 must be delivered by 9:00
# Truck 2 packages: [6, 25, 28, 32] delayed until 9:05, 6 & 25 must be delivered by 10:30
# Truck 3 packages: deadline by EOD and no special note
truck1 = Truck(1, 18, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", timedelta(hours=8))
truck2 = Truck(2, 18, [2, 3, 6, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39], 0.0, "4001 South 700 East", timedelta(hours=9, minutes=5))
truck3 = Truck(3, 18, [4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26], 0.0, "4001 South 700 East", timedelta(hours=11))


# Function to deliver packages on a given truck using nearest neighbor algorithm
def truckDeliverPackages(truck):
    # Create a list for all packages that are not delivered yet
    notDelivered = []
    # Append the list with packages from the hash table
    for packageID in truck.packages:
        package = packageHashTable.search(packageID)
        notDelivered.append(package)
    # Clear packages from truck after appending the new list
    truck.packages.clear()

    # Loop through the list until no package left
    while len(notDelivered) > 0:
        nextAddress = 2000
        nextPackage = None
        for package in notDelivered:
            # Prioritize package 6 & 25 which must be delivered by 10:30
            if package.id in [6, 25]:
                nextAddress = distanceBetween(address(truck.address), address(package.address))
                nextPackage = package
                break
            # Assign the nearest package to be delivered next
            if distanceBetween(address(truck.address), address(package.address)) <= nextAddress:
                nextAddress = distanceBetween(address(truck.address), address(package.address))
                nextPackage = package
        # Add the nearest package to truck list
        truck.packages.append(nextPackage.id)
        # Remove the same package from notDelivered list
        notDelivered.remove(nextPackage)
        # Update the mileage traveled
        truck.mileage += nextAddress
        # Update the current location of the truck
        truck.address = nextPackage.address
        # Update the time taken to deliver the package
        truck.time += timedelta(hours=nextAddress / 18.0)
        # Track the delivery time of the package when the truck arrives
        nextPackage.deliveryTime = truck.time
        # Track the departure time of the package when the truck leaves
        nextPackage.departureTime = truck.departureTime
        # Track which truck delivering the package
        nextPackage.truckNumber = truck.truckNumber


# Load trucks to leave to deliver the packages
truckDeliverPackages(truck1)
truckDeliverPackages(truck2)
# Make sure truck 3 won't leave until first two trucks delivered all the packages
truck3.departureTime = min(truck1.time, truck2.time)
truckDeliverPackages(truck3)

while True:
    # Provide user interface
    print("\nWestern Governors University Parcel Service (WGUPS)")
    print("---------------------------------------------------")
    # Print total mileage traveled by all trucks
    print("Total mileage traveled:", (truck1.mileage + truck2.mileage + truck3.mileage), "miles")

    try:
        # Ask user to select a menu option
        userInput = int(input("""\nPlease select a menu option:
1. View all packages delivered by WGUPS
2. View status of package(s) at a specific time
3. Exit the program\n"""))
        while userInput != 3:
            try:
                if userInput == 1:
                    # Print all packages delivered by WGUPS
                    print("Packages delivered:")
                    # Track status of all packages delivered by all trucks
                    for pID in range(1, 41):
                        package = packageHashTable.search(pID)
                        package.updateStatus(truck3.time)
                        print(str(package) + " by Truck " + str(package.truckNumber))
                    break
                elif userInput == 2:
                    # Ask user to enter a specific time to view status of packages
                    timeInput = input("Please enter a time to check the status of package(s), using format (HH:MM):\n")
                    (h, m) = timeInput.split(':')
                    userTime = timedelta(hours=int(h), minutes=int(m))
                    try:
                        # Ask user to view a single package or all packages
                        viewInput = int(input("""Please select an option to check the status of package(s):
1. View an individual package by package ID
2. View all packages\n"""))
                        if viewInput == 1:
                            # Ask user to input package ID
                            idInput = [int(input("Please enter a package ID:\n"))]
                        elif viewInput == 2:
                            idInput = range(1, 41)
                        # Print status of packages
                        print("Status of package(s) as of " + str(userTime) + ":")
                        # Track status of all packages upon a specific time
                        for pID in idInput:
                            package = packageHashTable.search(pID)
                            package.updateStatus(userTime)
                            print(str(package))
                        break
                    except ValueError:
                        print("Invalid input! Please try again.")
            except ValueError:
                print("Invalid input! Please try again.")
        if userInput == 3:
            # Exit the program
            exit()
    except ValueError:
        print("Invalid input! Please try again.")
