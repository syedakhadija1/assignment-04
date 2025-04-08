def get_user_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        numbers.append(int(user_input))
    return numbers

def count_numbers(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

def print_counts(counts):
    for num, count in counts.items():
        print(f"{num} shows up {count} time(s).")

def main():
    user_numbers = get_user_numbers()
    number_counts = count_numbers(user_numbers)
    print_counts(number_counts)

if __name__ == '__main__':
    main()
