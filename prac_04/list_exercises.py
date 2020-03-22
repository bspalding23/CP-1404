
NUMBERS = 5


def main():
    numbers = []
    for number in range(NUMBERS):
        amount_of_numbers = int(input("Please enter a number\n"))
        numbers.append(amount_of_numbers)

    print("The first number is: {}".format(numbers[0]))
    print("The last number is: {}".format(numbers[-1]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    print("The average number is: {}".format(sum(numbers) / len(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Please enter in your username\n")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()
