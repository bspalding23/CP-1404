
# 1.
name_file = open("name.txt", "w")
name_file.write(input("Please enter your name\n"))
name_file.close()


# 2.
name_file = open("name.txt", "r")
print("Your name is {}".format(name_file.read()))
name_file.close()
# I didn't strip as no extra characters were added I thought.
# I input values on either side of "{}" to check and there was no spacing, etc. Please tell me why I'm wrong if I am.


# 3.
number_file = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
number_file.close()
print("Total for first two lines of numbers: {}".format(number1 + number2))


# 4.
number_file = open("numbers.txt", "r")
total = 0
for line in number_file:
    total += int(line)
number_file.close()
print("Total of all numbers in file: {}".format(total))

# I noticed in some questions you were creating a variable and I didn't bother as it's shorter lines of code.
# It is however more beneficial to create it? Sorry for questions. Just want to get better and produce code as well as
# possible.

