import random




def get_choices():
    player_choice = input("enter a choice(rock, paper, scissors): ")
    options=["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices={"player": player_choice, "computer":computer_choice}
    return choices

def check_win(player ,computer):
    print(f"You chose {player} ,computer chose {computer}")
    if player==computer:
        return "Its a tie!!"
    elif player =="rock":
        if computer =="scissors":
            return "Rock smashes scissors! You Win!!"
        else:
            return "Paper covers rock! You lose."
        
    elif player =="paper":
        if computer =="rock":
            return "Paper covers rock! You Win!!"
        else:
            return "Scissros cuts paper! You lose."
        
    elif player =="scissors":
        if computer =="paper":
            return "Scissors cut paper! You Win!!"
        else:
            return "Rock smashes scissors! You lose."
    

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

#If we put ; after a statement and then write another statement, both the statements will still run.
#eg:: name="Shivani" ; print(name)