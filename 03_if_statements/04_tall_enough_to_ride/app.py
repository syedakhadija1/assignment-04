MINIMUM_HEIGHT = 50  # minimum required height

def main():
    height = float(input("How tall are you? "))

    if height >= MINIMUM_HEIGHT:
        print("Awesome! You're tall enough to enjoy the ride!")
    else:
        print("Oops! You're not quite tall enough yet — maybe next year!")

if __name__ == '__main__':
    main()
