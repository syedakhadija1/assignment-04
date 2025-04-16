import random
import string
from colorama import Fore, Style, init

def generate_password(length=12):
    """Generate a random password with a given length."""
    if length < 8:
        print("Password length is too short. Setting it to 8 characters.")
        length = 8
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=length))
    return password

def get_user_input():
    """Prompt the user to enter the number of passwords and their length."""
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the length of the password: "))
        return num_passwords, password_length
    except ValueError:
        print("Please enter valid numbers.")
        return get_user_input()

def display_passwords(num_passwords, password_length):
    """Generate and display the requested passwords."""
    print("\nGenerated Passwords:")
    for i in range(1, num_passwords + 1):
        password = generate_password(password_length)
        print(f"Password {i}: {password}")

def main():
    print("Welcome to the Password Generator!\n")
    num_passwords, password_length = get_user_input()
    display_passwords(num_passwords, password_length)

if __name__ == "__main__":
    main()
