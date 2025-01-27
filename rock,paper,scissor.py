import random
def get_user_choice():
    user_choice = input("enter your choice(rock,paper,scissors):").lower()
    while user_choice not in ("rock", "paper","scissors"):
        user_choice = input("invalid choice. please try again(rack, paper, scissors):")
    return user_choice
def get_computer_choice():
    choices = ("rock","paper","scissors")
    return random.choice(choices)
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return ("its a tie!")
        
    elif(user_choice=="rock" and computer_choice=="scissors") or\
        (user_choice=="scissors" and computer_choice=="paper") or\
        (user_choice=="paper" and computer_choice=="rock"):
         return ("you win!")
    
    else:
        return ("you lose!")
        
def play_game():
        print("welcome to rock,paper,scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"you chose:{user_choice}")
        print(f"computer chose:{computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
play_game()
