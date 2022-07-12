######################################################################
# Script Name: Assignment5.py
# Title: Assignment 5 Code File
# Description: SCP220 Week 5 Assignment. 
# IDE of your choice: PyCharm
# Author: Andre Johnson
# Date: February 18, 2022
######################################################################
standard1 = [12.25, 18.0, 27.125]
metric1 = []


# TODO 1.1: Using function parameters. Delete 'pass' and modify the function to
# TODO 1.1: convert the values in the standard1 list (inch) and store in the metric1 list (mm).
# TODO 1.1: Do not print the data within the function, this will be done in TODO 2.1.
# TODO 1.1: DO NOT USE THE GLOBAL KEYWORD OR FUNCTION IN THIS STEP!


def standard_to_metric(inches, mm):
    for i in range(len(inches)):
        mm.append(inches[i] * 25.4)
    return mm


# TODO 1.2: Run the above function, passing in standard1 and metric1 as the parameter arguments.

standard_to_metric(standard1, metric1)

# TODO 2.1: Write a function that uses a loop to print the original and converted values in parallel with each other,
# TODO 2.1: each element and its converted value on each line with appropriate headings. Round to 2 decimal places.
# TODO 2.1: Only print the standard1 and metric1 functions.


def print_data(standard, metric):
    for i in range(len(standard)):
        print(f"{standard[i]:.2f} in = {metric[i]:.2f} mm")


# TODO 2.2:  Run the above function.
print_data(standard1, metric1)

# TODO 3.1: Using global variables and the 'globals()' function or 'global' keyword, modify the function
# TODO 3.1: below to convert the standard values in the standard2 list and store in the metric2 list.
# TODO 3.1: DO NOT USE THE PARAMETERS IN THIS STEP. Do not print the data within this function, this will
# TODO 3.1: done in TODO 3.3.


def standard_to_metric2():
    global standard2
    global metric2
    standard2 = [22.4, 60.0, 98.5]
    metric2 = []
    for i in range(len(standard2)):
        metric2.append(standard2[i] * 25.4)
    return metric2


# TODO 3.2: Run the above function.
standard_to_metric2()

# TODO 3.3: Using the function you defined in 2.1, print the results of your second conversion function.
# TODO 3.3: NOTE: DO NOT re-create the print_data() function! Depending on how you originally set up the
# TODO 3.3: print_data() function, you may need to go back and modify the print_data(). Only print standard2
# TODO 3.3: and metric2.
print()

print_data(standard2, metric2)


# TODO 4: Using the function 'main' below, repeat the above process from within the scope of main.
# TODO 4: Perform the conversions by calling the functions you wrote earlier, print the results using the
# TODO 4: function you defined earlier. BEST PRACTICE: Be sure to use the 'global' keyword or the 'globals()'
# TODO 4: functions, try not to access the global variables.
print()


def main():
    metric1 = []
    standard1.extend(standard2)
    all_metric = standard_to_metric(standard1, metric1) + standard_to_metric2()
    print_data(standard1, all_metric)


main()
