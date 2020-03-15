
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS_WILDCARD = "#"
CONSONANTS_WILDCARD = "%"
CHOICES = "#%cv"


def main():
    word_format = input("Please enter in a word format\n")
    while not is_valid_format(word_format):
        word_format = input("Please enter a word format using appropriate choices\n")

    word = ""
    for kind in word_format:
        if kind == VOWELS_WILDCARD:
            char_size = random.randint(1, 6)
            for i in range(char_size):
                word += random.choice(VOWELS)
        elif kind == CONSONANTS_WILDCARD:
            char_size = random.randint(1, 6)
            for i in range(char_size):
                word += random.choice(CONSONANTS)
        elif kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print("Password is: {}".format(word))


def is_valid_format(word_format):
    for char in word_format:
        if char not in CHOICES:
            return False
    return True


main()
