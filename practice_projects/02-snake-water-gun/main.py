import random

# ==============================================================================
# SNAKE WATER GUN GAME
# 
# Game Rules:
# - Snake vs Water -> Snake drinks Water (Snake Wins) -> 1 beats -1
# - Water vs Gun   -> Water douses Gun (Water Wins)   -> -1 beats 0
# - Gun vs Snake   -> Gun shoots Snake (Gun Wins)     -> 0 beats 1
# ==============================================================================

# Computer randomly chooses: 1 (Snake), -1 (Water), or 0 (Gun)
computer = random.choice([-1, 0, 1])

# User input & mappings
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Validate user input before processing
if youstr in youDict:
    you = youDict[youstr]

    # Display choices
    print(f"\nYou Chose: {reverseDict[you]}")
    print(f"Computer Chose: {reverseDict[computer]}\n")

    # Game logic comparison
    if computer == you:
        print("It's a draw! ")

    else:
        if computer == -1 and you == 1:
            print("You Win! ")

        elif computer == -1 and you == 0:
            print("You Lose! ")

        elif computer == 1 and you == -1:
            print("You Lose! ")

        elif computer == 1 and you == 0:
            print("You Win! ")

        elif computer == 0 and you == -1:
            print("You Win! ")

        elif computer == 0 and you == 1:
            print("You Lose! ")

        else:
            print("Something went wrong!")

else:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")