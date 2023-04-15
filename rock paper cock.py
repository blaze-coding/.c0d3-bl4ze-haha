import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock is 0 paper is 1 scissors is 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won 1 brain cell!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won 1 brain cell!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won 1 brain cell!")
        user_wins += 1
        continue

    else:
        print("You lost 1 braincell, idiot!")
        computer_wins += 1

print("You won gay ass", user_wins, "times.")
print("The computer won gay ass", computer_wins,"times.")
input("Goodbye, my bitchless friend!")