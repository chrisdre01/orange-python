######################################################################
# Script Name: Assignment3.py
# Title: Assignment 3 Code File
# Description: Code file for SCP220 Week 3 Assignment. Re-write into
# IDE of your choice. !!Contains errors for you to fix!!
# Author: Nathan Braun [student, update with your name.]
# Date:  March 20, 2020 [student, update with current date.]
######################################################################

payRates = [15.8, 16.0, 17.45, 15.8, 20.2]
timeCards = [35.75, 42.0, 41.0, 40.0, 39.5]
payAmounts = [0, 0, 0, 0, 0]

count = 0
pay = 0.0
hours = 0.0

# TODO 1: Complete the logic.
# TODO 1.1 : Using what you learned from the week's readings, complete the while loop to
# TODO 1.1 : process all timecards with the associated pay rates in the above lists. Make sure to use a
# TODO 1.1 : decision structure to determine if overtime pay is required and
# TODO 1.1 : calculate overtime pay, which is: OTpay = (payRate * 40) + [(1.5 * payRate) * (timeCards - 40)]
# TODO 1.2 : Store each calculated pay amounts in the PayAmounts list.


while count < 5:
    if timeCards[count] > 40:
        hours = timeCards[count] - 40
        pay = (payRates[count] * 40) + ((1.5 * payRates[count]) * hours)
    else:
        pay = payRates[count] * timeCards[count]
    payAmounts[count] = pay
    count += 1


# TODO 2: print the list of pay rates, hourly rates, and pay amounts for each employee.
count = 0
while count < 5:
    print(
        "Employee",
        f"{count}:\n",
        f"Pay Rate: {payRates[count]:.2f}\n",
        f"Hours Worked: {timeCards[count]:.2f}\n",
        f"Check Amount: {payAmounts[count]:.2f}",
    )
    count += 1
