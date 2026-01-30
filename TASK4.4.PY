
import random

choices = {1: "rock", 2: "paper", 3: "scissors"}

while True:
    print("\n1.Rock  2.Paper  3.Scissors  4.Exit")
    user_input = int(input("Choose your option: "))

    if user_input == 4:
        print("Game ended.")
        break

    user_choice = choices.get(user_input)
    computer_choice = random.choice(list(choices.values()))

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

