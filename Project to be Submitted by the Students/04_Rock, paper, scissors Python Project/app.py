import random
from colorama import init, Fore, Style

init()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return Fore.YELLOW + "It's a tie!"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return Fore.GREEN + "You win!"
    
    return Fore.RED + "Computer wins!"

def play_game():
    print(Fore.CYAN + "\nWelcome to Rock, Paper, Scissors!")
    
    choices = ["rock", "paper", "scissors"]
    
    user_choice = input(Fore.YELLOW + "Enter your choice (rock, paper, or scissors): ").lower()

    while user_choice not in choices:
        print(Fore.RED + "Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input(Fore.YELLOW + "Enter your choice (rock, paper, or scissors): ").lower()

    computer_choice = random.choice(choices)
    print(Fore.MAGENTA + f"\nComputer chose: {computer_choice}")
   
    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")


if __name__ == "__main__":
    play_game()
