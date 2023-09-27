#Paper Rock Scissors lizard Spock PybyFry
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

while True:
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Try again dingus!")
        continue

    random_number = random.randint(0, 4)
    # rock: 0, paper: 1, scissors: 2, lizard: 3, spock: 4
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Rock crushes Scissors!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Paper covers Rock!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Scissors cuts Paper!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "lizard":
        print("Scissors decapitates Lizard!")
        user_wins += 1

    elif user_input == "lizard" and computer_pick == "paper":
        print("Lizard eats Paper!")
        user_wins += 1

    elif user_input == "lizard" and computer_pick == "spock":
        print("Lizard poisons Spock")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "lizard":
        print("Rock crushes Lizard!")
        user_wins += 1

    elif user_input == "spock" and computer_pick == "scissors":
        print("Spock smashes Scissors!")
        user_wins += 1

    elif user_input == "spock" and computer_pick == "rock":
        print("Spock vaporizes Rock!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "spock":
        print("Paper disproves Spock!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw")

    elif computer_pick == "rock" and user_input == "scissors":
        print("Rock crushes your Scissors!")
        computer_wins += 1

    elif computer_pick == "paper" and user_input == "rock":
        print("Paper covers your Rock!")
        computer_wins += 1

    elif computer_pick == "scissors" and user_input == "paper":
        print("Scissors cuts your Paper!")
        computer_wins += 1

    elif computer_pick == "scissors" and user_input == "lizard":
        print("Scissors decapitates your Lizard!")
        computer_wins += 1

    elif computer_pick == "lizard" and user_input == "paper":
        print("Lizard eats your Paper!")
        computer_wins += 1

    elif computer_pick == "lizard" and user_input == "spock":
        print("Lizard poisons your Spock")
        computer_wins += 1

    elif computer_pick == "rock" and user_input == "lizard":
        print("Rock crushes your Lizard!")
        computer_wins += 1

    elif computer_pick == "spock" and user_input == "scissors":
        print("Spock smashes your Scissors!")
        computer_wins += 1

    elif computer_pick == "spock" and user_input == "rock":
        print("Spock vaporizes your Rock!")
        computer_wins += 1

    elif computer_pick == "paper" and user_input == "spock":
        print("Paper disproves your Spock!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
