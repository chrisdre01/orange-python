######################################################################
# Script Name: Assignment4.py
# Title: Assignment 4 Code File
# Description: Code file for SCP220 Week 4 Assignment. Re-write into
# IDE of your choice. !!Contains errors for you to fix!!
# Author: Nathan Braun [student, update with your name.]
# Date:  March 26, 2020 [student, update with current date.]
######################################################################

dailyTemps = [[44, 51, 39], [34, 49, 40], [36, 52, 42], [42, 58, 49], [44, 63, 45]]

vehicleInventory = [
    {"make": "Chevrolet", "model": "Camaro", "year": 2019, "color": "red"},
    {"make": "Chevrolet", "model": "Tahoe", "year": 2017, "color": "Silver"},
    {"make": "Dodge", "model": "Durango", "year": 2012, "color": "White"},
]

# TODO 1: Print the dailyTemps values in a tabular format, i.e.
# TODO 1: only 3 values on each row. {HINT: Use nested loops}

for day in dailyTemps:
    for temp in day:
        print(temp, end="\t")
    print()

# TODO 2: Print the values within the vehicleInventory collection.
# TODO 2: Each vehicle should be separated with a blank line and have
# TODO 2: appropriate labels.{HINT: Use nested loops}
print()

for vehicle in vehicleInventory:
    for key, value in vehicle.items():
        print(key, value)
    print()


# TODO 3: Write a WHILE loop that prints the counter variable's value
# TODO 3: for each iteration. The loop should run 15 times, and increment by 3.

counter = 0
while counter < 15:
    print(counter)
    counter += 3


# TODO 4: Write a FOR loop that prints the counter variable's value
# TODO 4: for each iteration. The loop should run 75 times, and increment by 3.
print()

counter = 0
for num in range(75):
    counter += 3
    print(counter)
