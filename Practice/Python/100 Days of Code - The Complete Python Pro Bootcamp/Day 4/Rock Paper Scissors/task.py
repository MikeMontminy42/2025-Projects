import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImage = [rock,paper,scissors]

compChoice = random.randint(0,2)

userChoice = int(input("Enter your choice here (0 for Rock, 1 for Paper, and 2 for Scissors): "))

if userChoice >= 0 and userChoice <= 2:
    print(gameImage[userChoice])

if userChoice >= 3 or userChoice < 0:
    print("INVALID INPUT. AUTOMATIC LOSS.")
    exit()

print("Computer Choice: ")
print(gameImage[compChoice])

if userChoice == 0 and compChoice == 2:
    print("You won.")
elif userChoice == 2 and compChoice == 0:
    print("You lost.")
elif userChoice < compChoice:
    print("You lost.")
elif userChoice > compChoice:
    print("You won.")
elif userChoice == compChoice:
    print("Draw.")
