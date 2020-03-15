
MIN_LENGTH = 9

password = input("Please enter in a password, it must be at least 9 characters in length\n")

while len(password) < MIN_LENGTH:
    password = input("Please try again\nPassword was not 9 at least characters in length\n")

asterisks = ""
for char in password:
    asterisks += "*"
print(asterisks)
