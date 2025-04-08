PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    user_age = int(input("How old are you? "))

    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You meet the voting age requirement for Peturksbouipo, which is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"In Peturksbouipo, you must be at least {PETURKSBOUIPO_AGE} to vote — you’re not there yet.")

    if user_age >= STANLAU_AGE:
        print(f"You're old enough to vote in Stanlau, where the legal voting age is {STANLAU_AGE}.")
    else:
        print(f"Stanlau requires voters to be {STANLAU_AGE} or older. You’re not eligible yet.")

    if user_age >= MAYENGUA_AGE:
        print(f"You qualify to vote in Mayengua. Their voting age is {MAYENGUA_AGE}.")
    else:
        print(f"To vote in Mayengua, you need to be {MAYENGUA_AGE} years old. You haven’t reached that age yet.")

if __name__ == '__main__':
    main()
