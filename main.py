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

# def loadPackageData(filename):
