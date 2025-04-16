import random
from colorama import init, Fore, Style

init()


def computer_guess():
    print(Fore.CYAN + "\nWelcome to the enhanced Guess the Number game!")
    
    while True:
      
        try:
            low = int(input(Fore.YELLOW + "Enter the lowest number in your range: "))
            high = int(input(Fore.YELLOW + "Enter the highest number in your range: "))
            if low >= high:
                print(Fore.RED + "Please ensure that the lowest number is less than the highest number.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter valid numbers for the range.")

    print(Fore.GREEN + f"\nGreat! Think of a number between {low} and {high}, and I will try to guess it.")
    print(Fore.GREEN + "You can respond with: 'too high', 'too low', or 'correct'.")

    guesses = 0
    guess_history = []

    while True:
        guesses += 1
        
        guess = random.randint(low, high)
        guess_history.append(guess)  
        
        print(Fore.MAGENTA + f"\nAttempt {guesses}: Is your number {guess}?")

        user_input = input(Fore.YELLOW + "Enter 'too high', 'too low', or 'correct': ").lower()

        if user_input == 'too high':
            high = guess - 1
        elif user_input == 'too low':
            low = guess + 1
        elif user_input == 'correct':
            print(Fore.GREEN + f"\nYay! I guessed your number {guess} in {guesses} attempts!")
            print(Fore.CYAN + f"My guesses were: {', '.join(map(str, guess_history))}")
            break
        else:
            print(Fore.RED + "Invalid input! Please enter 'too high', 'too low', or 'correct'.")

        if high - low <= 1:
            print(Fore.YELLOW + f"\nWarning: The range is too small now! It seems your number should be {low} or {high}.")

        if user_input not in ['too high', 'too low', 'correct']:
            print(Fore.RED + "\nMake sure you enter 'too high', 'too low', or 'correct'.")

    play_again = input(Fore.CYAN + "\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        computer_guess()
    else:
        print(Fore.MAGENTA + "\nThanks for playing! Goodbye!")

computer_guess()
