import time
import random
continuegame = "yes"




def gameloop():
    playerpick = input("Rock, Paper or Scissors?").lower()
    if playerpick == "rock" or playerpick == "paper" or playerpick == "scissors":
        time.sleep(1)
        print("My turn to pick...")
        time.sleep(2)
        computerpick = random.choice(["rock", "paper", "scissors"])
        print(f"computer picked: {computerpick}")
        time.sleep(1)
        if playerpick == computerpick:
            print("It's a tie!")
        elif (playerpick == "rock" and computerpick == "scissors") or (playerpick == "paper" and computerpick == "rock") or (playerpick == "scissors" and computerpick == "paper"):
            print("You win!")
            time.sleep(3)
            return input("Do you want to play again? (yes or no)").lower()
        else:
            print("You lose!")
            time.sleep(3)
            return input("Do you want to play again? (yes or no)").lower()









intro = input("So, were gonna play rock paper scissors, respond to this message with (yes, no), depending on if you want to know the rules.")
if intro == "yes":
    print("No problem, so, you just type in (rock or paper or scissors), and I will do the same, rock beats scissors, scissors beats paper, and paper beats rock. Good luck!")
    time.sleep(2)
    continuegame = "yes"
    
elif intro == "no":
    print("Alright, let's get started!")
    time.sleep(1)
    continuegame = "yes"



while continuegame == "yes":
    continuegame = gameloop()
else:
    print("were done")
    
    
    





