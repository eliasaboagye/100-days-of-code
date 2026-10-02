
import random
rock = """
      _________
_ _ _'   ______)
        (_______)
        (_______)
_ _ _   (______)
     .__(_____)

"""

paper = """
      _________
_ _ _'   ______)_____
             ________)
             _________)
_ _ _       ________)
     .____________)
"""

scissors = """
      _________
_ _ _'   ______)_____
             ________)
             _________)
_ _ _   (______)
     .__(_____)
"""


options = [rock, paper, scissors]
computer_choice = random.randint(0,2)
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if your_choice < 0 or your_choice >= 3:
    print("You typed an invalid number. You lose")
else:
    print(f"\nComputer Choice: \n{options[computer_choice]}")
    print(f"Your Choice: \n{options[your_choice]}\n")

if your_choice == computer_choice:
    print("It's a tie")
elif (your_choice + 1) % 3 == computer_choice:
    print("You lose")
else:
    print("You won")