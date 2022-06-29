import random

options = ["rock", "paper", "scissors"]
flag = True
ties = 0
Losses = 0
Wins = 0
while(flag == True):
    pchoice = input("Enter your choice (rock, paper, scissors, or END to end the game): ")
    compChoice = options[random.randint(0,2)]
    print(compChoice)
    if(pchoice == "END"):
        flag = False
    elif(compChoice ==pchoice ):
        print("tie") 
        ties +=1
    elif(compChoice == "rock" and pchoice == "scissors"):
        print("you lose")
        Losses +=1
    elif(compChoice == "rock" and pchoice == "paper"):
        print("You Win")
        Wins +=1
    elif(compChoice == "paper" and pchoice == "scissors"):
        print("you Win")
        Wins +=1
    elif(compChoice == "paper" and pchoice == "rock"):
        print("You Lose")
        Losses +=1
    elif(compChoice == "scissors" and pchoice == "rock"):
        print("you win")
        Wins +=1
    elif(compChoice == "scissors" and pchoice == "paper"):
        print("You Lose")
        Losses +=1
    else:print("invaild input")
    print("Wins:  ", Wins ,", Losses: ", Losses, ", ties: ",ties,"\n")