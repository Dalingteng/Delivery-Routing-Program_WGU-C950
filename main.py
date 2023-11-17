# Author: Sochandaling Teng
# Student ID: 010309126

import csv
import datetime
from hashtable import HashTable
from package import Package
from truck import Truck

with open("csv/package.csv") as packageCSV:
    PackageCSV = csv.reader(packageCSV)
    PackageCSV = list(PackageCSV)
with open("csv/distance.csv") as distanceCSV:
    DistanceCSV = csv.reader(distanceCSV)
    DistanceCSV = list(DistanceCSV)
with open("csv/address.csv") as addressCSV:
    AddressCSV = csv.reader(addressCSV)
    AddressCSV = list(AddressCSV)


# Create package object from package csv file to load into the hash table
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
            pStatus = package[7]
        # Create package object
        p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)
        # Insert package object into the hash table
        packageHashTable.insert(pID, p)


# Find distance between two addresses
def distanceBetween(address1, address2):
    distance = DistanceCSV[address1][address2]
    if distance == '':
        distance = DistanceCSV[address2][address1]
    return float(distance)


# Get address number from address csv file
def address(a):
    for row in AddressCSV:
        if a in row[2]:
            return int(row[0])


# Create hash table for packages
packageHashTable = HashTable()

# Load packages into the has table
loadPackageData('csv/package.csv')

# Create truck object

