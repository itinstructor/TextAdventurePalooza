"""
    Name: text_adventure_palooza.py
    Author: William A Loring
    Created: 12/29/2021
    Purpose: A text adventure tutorial
"""
import sys


def main():
    # Start the game
    start()


#---------------------------- PLAY AGAIN ----------------------------#
def play_again():
    print("\nDo you want to play again? (y or n)")

    # Convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        sys.exit()


#---------------------------- GAME OVER -----------------------------#
def game_over(reason):
    # Print the "reason" in a new line (\n)
    print("\n" + reason)
    print("Game Over!")
    # ask player to play again or not by activating play_again() function
    play_again()


#------------------------- DIAMOND ROOM ----------------------------#
def diamond_room():
    # some prompts
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would Mindi do?")
    print("(1) Take some diamonds and run through the door.")
    print("(2) Just go through the door.")

    # take input()
    answer = input(">> ")

    if answer == "1":
        # the player is dead, call game_over() function with the "reason"
        game_over(
            "They were cursed diamonds! The building collapsed, you lose!")
    elif answer == "2":
        # the player won the game
        print("\nIt pays not to be greedy. Congratulations, you win the game!")
        # activate play_again() function
        play_again()
    else:
        # call game_over() with "reason"
        game_over("Go and learn how to type a number.")


#----------------------------- MONSTER ROOM ----------------------------#
def monster_room():
    # some prompts
    # '\n' is to print the line in a new line
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.")
    print("Behind the monster, there is another door.")
    print("What would Dylan do?")
    print("(1) Go through the door silently.")
    print("(2) Kill the monster and show your courage!")

    # take input()
    answer = input(">> ")

    if answer == "1":
        # lead him to the diamond_room()
        diamond_room()
    elif answer == "2":
        # the player is dead, call game_over() with "reason"
        game_over("The monster was hungry, too bad..")
    else:
        # game_over() with "reason"
        print("Invalid choice: Try again.")
        monster_room()


#------------------------------ BEAR ROOM -------------------------------#
def bear_room():
    """
        Tell the store of the bear room
    """
    # Prompt the user for input
    print("\nThere is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating tasty honey!")
    print("What does Laurie do?")
    print("(1) Take the honey.")
    print("(2) Taunt the bear.")

    # Get user input
    answer = input(">> ")

    if answer == "1":
        # The player is dead!
        game_over("The bear ate you for lunch.")
    elif answer == "2":
        # Lead him to the diamond_room()
        print("\nThe bear moved from the door. You can go through it now!")
        monster_room()
    else:
        # Else call game_over() function with the "reason" argument
        print("Invalid choice: Try again.")
        bear_room()


#--------------------------- START ----------------------------#
def start():
    first_room = (
        "(1) Run away!",
        "(2) Open the big door",
        "(3) Open the small door",
        "(4) Do nothing"
    )
    first_room_rewards = (
        "You live to run away another day.",
        "You walk into a room . . . . . ",
        "You are shrunk to half your size.",
        "You sit for a 100 years gathering dust"
    )

    print("The brave adventurers, Laurie, Mindi, and Dylan,")
    print("are in a dark cave with only a single small candle for light.")
    print("Your treasure map shows 4 choices.")

    for i in range(4):
        print(first_room[i])

    action = int(input(">> "))

    print(first_room_rewards[action - 1])
    if action - 1 == 1:
        bear_room()
    else:
        game_over()


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
