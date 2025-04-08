import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0

    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")
        
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is: {your_num}")

        choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()

        if choice == "higher" and your_num > computer_num:
            print(f"You were right! The computer's number was {computer_num}.")
            your_score += 1
        elif choice == "lower" and your_num < computer_num:
            print(f"You were right! The computer's number was {computer_num}.")
            your_score += 1
        else:
            print(f"Oops! That's incorrect. The computer's number was {computer_num}.")
        
        print(f"Your score is: {your_score}")
        print('--------------------------------')

    print("Thanks for playing!")
    print(f"Your final score is: {your_score}")

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
