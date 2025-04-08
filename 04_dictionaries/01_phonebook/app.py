def read_phone_numbers():
    """
    User se names aur numbers input leta hai aur phonebook dictionary mein store karta hai.
    """
    phonebook = {}  

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Phonebook ke saare names aur numbers print karta hai.
    """
    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    User ko phonebook mein naam search karne ka option deta hai aur number dikhaata hai.
    """
    while True:
        name = input("\nEnter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name}'s number is: {phonebook[name]}")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)



if __name__ == '__main__':
    main()
