# BASIC CAR INFO DATA FILE #
# MIKE MONTMINY #
# START: 04/25/2025 @ 19:20 #
# END: EVENTUALLY (Off and on coding) #
# LAST EDITED: 04/28/2025 @ 13:37 #

# IMPORTING SYS FOR EXIT AFTER ERROR

# FUNCTION TO LOAD THE DEALERSHIP INVENTORY
def loadInventory():
    currentInventory = []
    try:
        with open ('carInfo.txt', 'r') as file:
            currentInventory = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("FILE NOT FOUND. CREATE ONE BEFORE STARTING.")
    return currentInventory

# FUNCTION TO SAVE DEALERSHIP INVENTORY AFTER ANY CHANGES MADE
def saveInventory(databaseName, currentInventory):
    with open (databaseName, 'w') as file:
        for vehicle in currentInventory:
            file.write(vehicle + "\n")

# FUNCTION TO REMOVE VEHICLE FROM DEALERSHIP INVENTORY
def removeVehicle(databaseName, currentInventory):
    if not currentInventory:
        # Prints an 'error' message if there are no vehicles within the data file.
        print("NO VEHICLES TO REMOVE\n")
        return
    printInventory(currentInventory)

    try:
        # Prompts user to enter the index of the vehicle in the database to remove
        removeIndex = int(input("Enter vehicle index to remove said vehicle: "))
        if 1 <= removeIndex <= len(currentInventory):
            removeVehicle = currentInventory.pop(removeIndex - 1)
            saveInventory(databaseName, currentInventory)
            # Confirms removal
            print(f"REMOVED: {removeVehicle}\n")
        else:
            # Error if a non-existent index is entered
            print("INVALID INDEX")
    # Prints error if something other than an integer is entered by the user
    except ValueError:
        print("ENTER INTEGERS ONLY")

# MENU OPTIONS FOR DATABASE CONTROL
def menuOptions():
    print(f"\nDealership Inventory Database\n")
    print(f"1. ADD new vehicle to database\n")
    print(f"2. REMOVE vehicle from database\n")
    print(f"3. SEARCH for vehicle in database\n")
    print(f"4. PRINT all vehicles in database\n")
    print(f"0. EXIT database\n")

# ASKS FOR INPUT AND THEN PRINTS THE NEWLY ADDED VEHICLE INFO
def carInfo():
    while True:
        try:
            carYear = int(input("Enter Model Year: "))
            break
        # Throws an error if anything other than an integer is entered by the user
        except ValueError:
            print("ENTER INTEGERS ONLY")

    carMake = input("Enter Vehicle Make: ").strip()
    carModel = input("Enter Model Name: ").strip()
    carColor = input("Enter Vehicle Color: ").strip()
    carExtras = input("Enter Extra Features: ").strip()
    newVehicle = f"{carYear} {carMake} {carModel} in {carColor} with {carExtras}"
    return newVehicle

# FUNCTION TO ADD VEHICLE TO DEALERSHIP INVENTORY
def addVehicle(databaseName, currentInventory):
    vehicle = carInfo()
    # Adds the newly entered vehicle to the currentInventory vector
    currentInventory.append(vehicle)
    saveInventory(databaseName, currentInventory)
    # Prints out the data to allow for user to check over and remove if needed.
    print(f"\nVehicle Data Added: {vehicle}\n")

# FUNCTION TO PRINT CURRENT DEALERSHIP INVENTORY
def printInventory(currentInventory):
    if not currentInventory:
        # Prints an error if there are no vehicles in the data file.
        print("NO CURRENT INVENTORY")
    else:
        print("Current Inventory: ")
        for index, vehicle in enumerate(currentInventory, start = 1):
            print(f"{index}. {vehicle}")

# FUNCTION TO SEARCH FOR SPECIFIC CARS FITTING A GIVEN PARAMETER
def searchInventory(currentInventory):
    searchMetric = input("Enter item to search for(Color, Year, Make, Model, or Extras: ").strip().lower()
    searchResults = []
    for index, vehicle in enumerate(currentInventory, start = 1):
        if searchMetric in vehicle.lower():
            searchResults.append((index, vehicle))

    if searchResults:
        print("SEARCH RESULTS: \n")
        for index, vehicle in searchResults:
            print(f"{index}. {vehicle}")
    else:
        # Prints an error if there are no matching vehicles in the database
        print("NO MATCHING VEHICLES\n")

# THE MAIN FUNCTION OF THE PROGRAM
def main():
    databaseName = 'carInfo.txt'
    currentInventory = loadInventory()

    print(f"Current Inventory:")
    if currentInventory:
        for index, vehicle in enumerate(currentInventory, start=1):
            print(f"{index}. {vehicle}")
    else:
        # Prints an error stating there are no vehicles within the inventory data file
        print("NO CURRENT INVENTORY")
    while True:
        menuOptions()
        userMenuChoice = input('Enter a menu choice:')

        if userMenuChoice == '1':
            addVehicle(databaseName, currentInventory)

        elif userMenuChoice == '2':
            removeVehicle(databaseName, currentInventory)

        elif userMenuChoice == '3':
            searchInventory(currentInventory)

        elif userMenuChoice == '4':
            printInventory(currentInventory)

        elif userMenuChoice == '0':
            saveInventory(databaseName, currentInventory)
            print(f"\nEXITING DATABASE\n")
            break

        else:
            # Prints an error if something other than the given menu choices is entered by the user
            print("INVALID CHOICE. CHOOSE FROM ABOVE OPTIONS.")

main()
