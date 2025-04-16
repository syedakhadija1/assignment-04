import time
import threading
from colorama import init, Fore, Style

init()

def countdown_timer(seconds):
    print(Fore.CYAN + "\nCountdown Timer")
    print(Fore.YELLOW + f"Starting the countdown from 1 to {seconds}...\n")

    for i in range(1, seconds + 1):
        print(Fore.GREEN + str(i))  # Prints numbers from 1 to the user-defined time
        time.sleep(1)

    print(Fore.GREEN + "Time's up! 🎉")

def get_input():
    print(Fore.GREEN + "Enter the number of seconds for the countdown timer:")

    while True:
        try:
            seconds = int(input(Fore.YELLOW + "Seconds: "))
            if seconds <= 0:
                print(Fore.RED + "Please enter a positive number greater than zero.")
            else:
                return seconds
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")

def main():
    print(Fore.CYAN + "Welcome to the Countdown Timer!\n")
    while True:
        seconds = get_input()
        countdown_timer(seconds)

        play_again = input(Fore.GREEN + "Would you like to start another timer? (yes/no): ").lower()
        if play_again != "yes":
            print(Fore.MAGENTA + "Thanks for using the Countdown Timer! Goodbye!")
            break

if __name__ == "__main__":
    main()
