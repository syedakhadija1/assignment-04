import random
import time


def guess_the_number():
    print("\nWelcome to Guess the Number!")

    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    
    if difficulty == 'easy':
        max_number = 50
        max_attempts = 10
    elif difficulty == 'medium':
        max_number = 100
        max_attempts = 8
    else:
        max_number = 200
        max_attempts = 5
    
    number_to_guess = random.randint(1, max_number)
    attempts = 0
    start_time = time.time()

    print(f"\nI have picked a number between 1 and {max_number}. Can you guess it?")
    print("Tip: Try narrowing down the range with each guess!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1
            
            
            if attempts == 3:
                print(f"Hint: The number is divisible by {random.choice([2, 3, 5, 7, 11])}.")
            elif attempts == 5:
                print(f"Hint: The number is {'even' if number_to_guess % 2 == 0 else 'odd'}.")

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"\nCongratulations! You've guessed the number in {attempts} attempts and {total_time} seconds.")
                print(random.choice(["Great job!", "You're awesome!", "Fantastic guess!"]))
                break
        except ValueError:
            print("Please enter a valid number.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"\nSorry! You've used all attempts. The correct number was {number_to_guess}.")

    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == 'yes':
        guess_the_number()
    else:
        print("Thank you for playing! Goodbye.")


guess_the_number()
