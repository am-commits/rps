import random


score = 0
keep_going = True

while keep_going == True:
 choices = ["Rock","Paper","Scissors"]
 choice = input("Choose your move, 'Score' to see your current score, or 'Finish' to end game. \n")
 cpu_choice = random.choice(choices)
 print(f"\nYou: {choice}, CPU: {cpu_choice}.\n")

 if choice == cpu_choice:
    print("Tie!")
    score = score
 elif choice == "Rock":
    if cpu_choice == "scissors":
        print("Win!")
        score = score + 1
    else:
        print("Loss!")
        score = score -1
 elif choice == "Scissors":
    if cpu_choice == "Paper":
        print("Win!")
        score = score + 1
    else:
        print("Loss!")
        score = score - 1
 elif choice == "Paper":
    if cpu_choice == "Rock":
        print("Win!")
        score = score + 1
    else:
        print("Loss!")
        score = score - 1
 elif choice == "Score":
    if score > 0:
        print ("You have won " + str(score) + " games")
    elif score < 0:
        print ("You have lost " + str(abs(score)) + " games")
    else:
        print ("The score is tied")
 elif choice == "Finish":
  keep_going =  False
  if score < 0:
        print ("Game ended. Your score is positive. You have won " + str(score) + " games")
  elif score > 0:
        print ("Game ended. Your score is negative. You have lost " + str(score) + " games")
  else:
        print ("The score was tied")
 else:
     print ("Invalid input. Please try again.")






