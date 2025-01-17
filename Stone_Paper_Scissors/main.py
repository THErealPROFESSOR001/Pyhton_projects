import random

def main():
    # Generate computer's random choice
    computer = random.randint(1, 3)

    # Instructions for the user
    print("INSTRUCTIONS:")
    print("1. You have to choose between 'stone', 'paper', or 'scissors'.")
    print("2. Any invalid input will result in an error.\n")

    # User input
    you = input("Choose (stone, paper, scissors): ").strip().lower()

    # Dictionaries for mapping choices
    dict = {"stone": 1, "paper": 2, "scissors": 3}
    reverse_dict = {1: "stone", 2: "paper", 3: "scissors"}

    # Validate user input
    you_choose = dict.get(you)
    if you_choose is None:
        print("Invalid input! Please choose 'stone', 'paper', or 'scissors'.")
        return

    # Get computer's choice
    computer_choose = reverse_dict[computer]

    # Print choices
    print(f"\nYou chose: {you}")
    print(f"Computer chose: {computer_choose}\n")

    # Determine the outcome
    if computer == you_choose:
        print("It's a Draw!")
    else:
        if (you_choose == 1 and computer == 3):  # Stone beats Scissors
            print("You won!")
        elif (you_choose == 2 and computer == 1):  # Paper beats Stone
            print("You won!")
        elif (you_choose == 3 and computer == 2):  # Scissors beat Paper
            print("You won!")
        else:
            print("You lost!")
            print("Better luck next time...")

# Prompt user to start or end the game
Run = input("Do you want to play this game?\nIF YES, Type 'start'\nIF NO, Type 'end'\n").strip().lower()
if Run == "start":
    main()
elif Run == "end":
    print("See you next time!!")
else:
    print("Invalid format...")
