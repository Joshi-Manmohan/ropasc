import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if player == 'quit':
            running = False
            break

    if not running:  # Exit the loop if the player chose to quit
        break

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("You Lose!")

print("Thanks for playing!")
