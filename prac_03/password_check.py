
MIN_LENGTH = 9


def main():
    password = get_password()

    print_password(password)


def print_password(password):
    asterisks = ""
    for char in password:
        asterisks += "*"
    print(asterisks)


def get_password():
    password = input("Please enter in a password, it must be at least 9 characters in length\n")
    while len(password) < MIN_LENGTH:
        password = input("Please try again\nPassword was not 9 at least characters in length\n")
    return password


main()
