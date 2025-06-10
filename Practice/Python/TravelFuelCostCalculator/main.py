# TRAVEL FUEL COST CALCULATOR #
# MIKE MONTMINY #
# START DATE: 04/25/2025 @ 16:20 #
# END DATE: 04/25/2025 @ 17:00 (Genuinely concerning amount of time for a total of 10 lines of code) #

def tripCost(milesDriven, averageMPG, costPerGallon):
    fuelCost = milesDriven /  averageMPG
    finalCost = fuelCost * costPerGallon
    return finalCost

def main():
    milesDriven = float(input("Enter Distance Driven (MILES): "))
    averageMPG = float(input("Enter Vehicle Average MPG: "))
    costPerGallon = float(input("Enter Cost Per Gallon: "))

    totalTripCost = tripCost(milesDriven, averageMPG, costPerGallon)
    print(f"\nEstimated Total Cost: ${totalTripCost:.2f}")
main()
