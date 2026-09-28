print("\t\tWELCOME TO TRESURE ISLAND!!\n\t  Your mission is to find the treasure.")

first_direction = input("You're at a crosss road. Where do you want to go? Type \"left\" or \"right\" \n")

if first_direction == "left":
    swim_or_wait = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat or Type \"swim\" to swim across. \n")
    if swim_or_wait == "wait":
        door_color = input("You arrive on the island unharmed. There is a house with three doors. One red, one yellow, one blue. Which color do you choose? \n")
        if door_color == "yellow":
            print("You win!!")
        elif door_color == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door_color == "red":
            print("You enter a room of fire. Game Over.")
        else:
            print("Game Over")
    else:
        print("Attack by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")