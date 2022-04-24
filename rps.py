import random

choices = ["Rock","Paper","Scissors"]
choice = input("Choose your move \n")
cpu_choice = random.choice(choices)

print(f"\nYou: {choice}, CPU: {cpu_choice}.\n")

if choice == cpu_choice:
    print("Tie!")
elif choice == "Rock":
    if cpu_choice == "scissors":
        print("Win!")
    else:
        print("Loss!")
elif choice == "Scissors":
    if cpu_choice == "paper":
        print("Win!")
    else:
        print("Loss!")
elif choice == "Paper":
    if cpu_choice == "rock":
        print("Win!")
    else:
        print("Loss!")

