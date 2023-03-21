import random

def roll_dice():
    """
    Simulates rolling a six-sided dice and returns the result.
    """
    return random.randint(1, 6)

def play_game():
    """
    Runs the dice roll game. Prompts the user to roll the dice and displays the result.
    """
    rolls = []
    roll_count = 0

    choice = input("Press enter to roll the dice, or type q to quit...").lower()
    while choice != "q":
        roll_result = roll_dice()
        rolls.append(roll_result)
        roll_count += 1
        print(f"You rolled a {roll_result}!")

        if roll_count == 0:
            print("Press enter to roll again, or type q to quit...")

        choice = input().lower()
        if choice == "q":
            break

    if rolls:
        print(f"Thanks for playing! You made {roll_count} rolls: {rolls}")
    else:
        print("Thanks for playing!")

print("Welcome to the dice roll game!")
play_game()
