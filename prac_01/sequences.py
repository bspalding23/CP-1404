
number1 = int(input("Please enter your first number\n"))
number2 = int(input("Please enter your second number\n"))

# inputs = ["x", "y"]
# for i in range(len(inputs)):
#     inputs[i] = int(input("Please enter an integer for {}\n".format(inputs[i])))
#     print(inputs[i])

even_numbers = []
odd_numbers = []
squared_numbers = []
for i in range(number1, number2 + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

    square_root_number = i ** 0.5
    if square_root_number % 1 == 0:
        squared_numbers.append(i)

print("Your even numbers between {} and {} are {}\n"
      "Your odd numbers between {} and {} are {}\n"
      "Your square numbers between {} {} are {}".format(number1, number2, even_numbers,
                                                        number1, number2, odd_numbers,
                                                        number1, number2, squared_numbers))





