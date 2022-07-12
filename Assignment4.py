# For this assignment, you will be modifying the used car dealer application from last week. There will be no code file provided for this assignment, you will be working from the previous week’s project files.
# !!VERSION CONTROL!!: Be sure to make a backup copy of your project folder before you begin work on this assignment.
# This week, you will be modifying your application to add two new menu items: Save Data, Load Data. The Save Data option will write the current vehicle data to a text file, overwriting any existing data. Load data will open the specified text file and read in the vehicle data into memory.
# Once you have the desired functionality, you will take screenshots of your program executing and the contents of your text file in order to demonstrate your program is able to save and load data to and from the text file. Paste your screenshots into a Word doc along with your completed code.


class Car:
    inventory = []

    # initializer with instance attributes
    def __init__(self, make, model, vin, mileage, price, features):
        self.make = make
        self.model = model
        self.vin = vin
        self.mileage = mileage
        self.price = price
        self.features = features

    # adds a new car to the inventory list
    def add_car(self):
        Car.inventory.append(self)

    # sets an attribute to a new value
    def edit_car(self, attribute):
        if attribute == "features":
            self.features = input("Enter new features: ").split(", ")
        else:
            setattr(self, attribute, input(f"Enter new {attribute}: "))

    # displays an individual car
    def display_car(self):
        print(
            f"Make: {self.make}, Model: {self.model}, VIN: {self.vin}, Mileage: {self.mileage}, Price: ${self.price}, Features: {self.features}"
        )

    # deletes a car from the inventory list
    def delete_car(self):
        Car.inventory.remove(self)

    # displays all cars in the inventory list
    def display_inventory():
        for num, car in enumerate(Car.inventory, start=1):
            print(
                f"{num}. Make: {car.make}, Model: {car.model}, VIN: {car.vin}, Mileage: {car.mileage}, Price: ${car.price}, Features: {car.features}"
            )


def main():
    print("\nInventory Tracker")
    print("================")
    print("1. Add a car")
    print("2. Edit a car")
    print("3. Delete a car")
    print("4. Display inventory")
    print("5. Save inventory data")
    print("6. Load inventory data")
    print("7. Exit")

    input_option = int(input("Please select an option: "))
    if input_option == 1:
        print("\nAdd a car")
        print("================")
        # get user input for car attributes
        make = input("Make: ")
        model = input("Model: ")
        vin = input("VIN: ")
        mileage = input("Mileage: ")
        price = input("Price: ")
        features = input("Features: ").split(", ")
        # create a new car object
        new_car = Car(make, model, vin, mileage, price, features)
        # add the new car to the inventory list
        new_car.add_car()
        print("\nUpdated inventory:")
        Car.display_inventory()
        continue_program()

    elif input_option == 2:
        print("\nEdit a car")
        print("================")
        Car.display_inventory()
        # get user input for car attributes
        car_to_edit = int(input("Enter the number of the car you would like to edit: "))
        attribute = input("Enter the attribute you would like to edit: ").lower()
        # get the car object from the inventory list
        # set the attribute to the new value
        Car.inventory[car_to_edit - 1].edit_car(attribute)
        # display the updated car
        print("\nUpdated vehicle info:")
        Car.inventory[car_to_edit - 1].display_car()
        continue_program()

    elif input_option == 3:
        print("\nDelete a car")
        print("================")
        Car.display_inventory()
        car_to_delete = int(
            input("Enter the number of the car you would like to delete: ")
        )
        # get the car object from the inventory list
        # delete the car from the inventory list
        Car.inventory[car_to_delete - 1].delete_car()
        # display the updated inventory
        print("\nUpdated inventory:")
        Car.display_inventory()
        continue_program()

    elif input_option == 4:
        print("\nDisplay inventory")
        print("================")
        Car.display_inventory()
        continue_program()

    elif input_option == 5:
        textfile = open("inventory.txt", "w")
        for car in Car.inventory:
            textfile.write(
                f"{car.make}, {car.model}, {car.vin}, {car.mileage}, {car.price}, {car.features}\n"
            )
        textfile.close()
        print("\nInventory data saved.")
        continue_program()

    elif input_option == 6:
        textfile = open("inventory.txt", "r")
        for line in textfile:
            line = line.strip().split(", ")
            make = line[0]
            model = line[1]
            vin = line[2]
            mileage = line[3]
            price = line[4]
            features = line[5:]
            new_car = Car(make, model, vin, mileage, price, features)
            new_car.add_car()
        textfile.close()
        print("\nInventory data loaded.")
        continue_program()

    elif input_option == 7:
        print("Exiting...")


def continue_program():
    continue_option = input("\nPress any key to continue or 'q' to quit: ")
    if continue_option == "q":
        print("Exiting...")
    else:
        main()

main()


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
