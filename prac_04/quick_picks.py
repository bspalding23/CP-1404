
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_GAME = 6


def main():
    quick_picks = int(input("Please enter how many quick picks you wish to generate\n"))
    while quick_picks <= 0:
        quick_picks = int(input("Please enter a number above 0"))

    for i in range(quick_picks):
        line = []
        for ii in range(NUMBERS_PER_GAME):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in line:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            line.append(number)
        line.sort()
        print(" ".join("{:<2}".format(number) for number in line))


main()
