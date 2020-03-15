"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

MIN_SCORE = 0
MAX_SCORE = 100


def main():
    score = float(input("Enter score: "))
    print(calculate_result(score))

    random_generated_score = random.randint(MIN_SCORE, MAX_SCORE)
    print(calculate_result(random_generated_score))


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
