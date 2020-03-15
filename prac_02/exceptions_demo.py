"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))

    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("You cannot divide by zero! Please use a different integer"))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


# Question 1.
#       A ValueError will occur if I input anything other than a integer. E.g. a string or float.

# Question 2
#       You will get a ZeroDivisionError when you input 0 for the denominator

# Question 3
#       Yeah you could nest a "while" statement inside the "try" statement to error check the denominator
