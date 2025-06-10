print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
userChoice = input("You have two options. You can go right or left. Take your pick: ")
if userChoice == "left" or userChoice == "Left" or userChoice == "LEFT":
    secondChoice = input("You can either take a swim or wait here for a little while. Your choice: ")

    if secondChoice == "wait" or secondChoice == "Wait" or secondChoice == "WAIT":
        thirdChoice = input("Now the hard part. Choose either the red, blue, or yellow door: ")

        if thirdChoice == "yellow" or thirdChoice == "Yellow" or thirdChoice == "YELLOW":
            print("GOOD NEWS! You managed to find the treasure and successfully beat the game!")
        elif thirdChoice == "red" or thirdChoice == "Red" or thirdChoice == "RED":
            print("You opened the door and managed to get torched by a flamethrower. GAME OVER.")
        elif thirdChoice == "blue" or thirdChoice == "Blue" or thirdChoice == "BLUE":
            print("You opened the door and ended up being eaten by a wild tiger. GAME OVER.")
        else:
            print("CHOOSE A VALID OPTION (RED, BLUE, or YELLOW)")

    elif secondChoice == "swim" or secondChoice == "Swim" or secondChoice == "SWIM":
        print("You managed to make it halfway across before getting swept away and drowning. GAME OVER.")
    else:
        print("CHOOSE A VALID OPTION (SWIM or WAIT)")

elif userChoice == "right" or userChoice == "Right" or userChoice == "RIGHT":
    print("You fell into a hidden 50 foot deep hole and died on impact. GAME OVER.")
else:
    print("CHOOSE A VALID OPTION (LEFT or RIGHT)")

