import random
import string
from colorama import init, Fore, Back, Style


init()

word_list = ["python", "hangman", "programming", "developer", "machine", "algorithm", "software", "technology"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])


def provide_hint(word, guessed_letters):
    unguessed_letters = [letter for letter in word if letter not in guessed_letters]
    if unguessed_letters:
        return random.choice(unguessed_letters)
    return None


def play_game():
    print(Fore.CYAN + "\nWelcome to Hangman!")
    print(Fore.GREEN + "You have 6 attempts to guess the word. Good luck!")
    
    score = {"wins": 0, "losses": 0}

    while True:
        word = choose_word()
        word_length = len(word)
        guessed_letters = []
        attempts = 6
        used_letters = set()
        print(Fore.YELLOW + f"\nThe word has {word_length} letters.")

      
        while attempts > 0:
            print(Fore.MAGENTA + "\nCurrent word: ", display_word(word, guessed_letters))
            print(Fore.LIGHTWHITE_EX + f"Used letters: {' '.join(sorted(used_letters))}")
            print(Fore.RED + f"Attempts left: {attempts}")
            print(Fore.LIGHTGREEN_EX + f"Score - Wins: {score['wins']} | Losses: {score['losses']}")

            guess = input(Fore.YELLOW + "Guess a letter or type 'hint' for a hint: ").lower()

            if guess == "hint":
                hint = provide_hint(word, guessed_letters)
                if hint:
                    print(Fore.CYAN + f"Hint: One of the missing letters is '{hint}'")
                else:
                    print(Fore.RED + "No more hints available!")
                continue

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(Fore.RED + "Invalid input! Please enter a single letter.")
                continue

            if guess in used_letters:
                print(Fore.YELLOW + f"You already guessed '{guess}'. Try a different letter.")
                continue

            used_letters.add(guess)
            if guess in word:
                guessed_letters.append(guess)
                print(Fore.GREEN + f"Good job! '{guess}' is in the word.")
            else:
                attempts -= 1
                print(Fore.RED + f"Sorry! '{guess}' is not in the word.")

            if all(letter in guessed_letters for letter in word):
                print(Fore.GREEN + f"\nCongratulations! You guessed the word '{word}'!")
                score["wins"] += 1
                break

        if attempts == 0:
            print(Fore.RED + f"\nGame Over! The word was '{word}'.")
            score["losses"] += 1

        play_again = input(Fore.YELLOW + "\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(Fore.LIGHTMAGENTA_EX + f"\nFinal Score - Wins: {score['wins']} | Losses: {score['losses']}")
            print(Fore.CYAN + "Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
