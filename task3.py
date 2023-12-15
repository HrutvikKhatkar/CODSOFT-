import random 

def get_your_choice():
    while True:
        your_choice = input("Choice Rock, Paper, Scissor : ").lower()
        if your_choice in ['rock', 'paper', 'scissor']:
            return your_choice
        else:
            print("Invalid choice. Please choose rock, paper, scissor.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def get_winner(your_choice,computer_choice):
    if(your_choice == computer_choice):
        return "It is a tie."
    elif((your_choice == "rock" and computer_choice == "scissor") or
         (your_choice== "scissor" and computer_choice == "paper") or
         (your_choice == "paper" and computer_choice == "rock")):
        return "You win!"
    else:
        return "You lose!"

your_score = 0
computer_score = 0
while True:
    print("Rock, Paper, Scissor")
    print("-----------------------")
    
    your_choice = get_your_choice()
    computer_choice = get_computer_choice()
    
    print("\nChoices - Your choice: "+your_choice+ "\n\t  Compute choice: "+computer_choice)
    
    result = get_winner(your_choice,computer_choice)
    print(result)
    
    if "win" in result:
        your_score+=1
    elif "lose" in result:
        computer_score+=1
    
    print("\nScore - You : "+ str(your_score) + " , Computer :" + str(computer_score))
    
    play_again = input("Do you want to play again ?  Yes(y) / No(n) : ").lower()
    print(play_again)
    if((play_again != 'yes') and (play_again != 'y')):
        print("\nThanks for playing.")
        break
    