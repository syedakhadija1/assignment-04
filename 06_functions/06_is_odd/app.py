def main():
    for i in range(10, 20):
        if is_odd(i):
            print(i, 'odd')
        else:
            print(i, 'even')

def is_odd(value: int):
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1

if __name__ == '__main__':
    main()
