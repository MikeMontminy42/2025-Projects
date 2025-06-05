print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

totalBill = 0


if size == "S" or size == "s":
    totalBill += 15
elif size == "M" or size == "m":
    totalBill += 20
elif size == "L" or size == "l":
    totalBill += 25
else:
    print("Enter a pizza size (S, M, or L): ")


if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        totalBill += 2
    else:
        totalBill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    totalBill += 1

print(f"Your final bill is: ${totalBill}.")