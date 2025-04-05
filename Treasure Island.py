print("Welcome to Treasure Island.")
print("Your mission is to find the threasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type  "LEFT" or "RIGHT": ').lower()

if choice1 == "left":
    choice2 = input('You\'ve to come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                            "There is house with 3 doors. One red, "
                            "one yellow and one blue."
                            "Which colour do you choose? ").lower()
        if choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You enter a room of beastes. Game over")
        else:
            print('Game over')
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell in to a hole. Game over")
