
MIN_NUMBER = 33
MAX_NUMBER = 127

# Create list with ascii code for values
ascii_values = []

for number in range(33, 127 + 1):
    ascii_values.append(chr(number))


# Creating table
for i in range(33, 127+1):
    print("{}{:>5}".format(i, ascii_values[i - 33]))


# Doing the conversion, etc.

valid_input = False
while not valid_input:
    try:
        chosen_number = int(input("PLease choose a number to find ascii code or character to find corresponding"
                                  "number\n"))
        if chosen_number not in range(MIN_NUMBER, MAX_NUMBER + 1):
            print("Please enter within the range of {} and {}".format(MIN_NUMBER, MAX_NUMBER))
        else:
            print("The ascii code for {} is {}".format(chosen_number, chr(chosen_number)))
            valid_input = True
    except ValueError:
        print(ord(str(chosen_number)))
        valid_input = True

# try:
#     while int(chosen_number) not in range(MIN_NUMBER, MAX_NUMBER + 1):
#         chosen_number = input("Please enter within the range of {} and {}\n".format(MIN_NUMBER, MAX_NUMBER))
# except ValueError:
#     pass
#
# if chosen_number.isdigit():
#     print("The ascii code for {} is {}".format(int(chosen_number), chr(int(chosen_number))))
# else:
#     print(ord(chosen_number))

# Code above could just hav eint(input()) and then have try and except have the char code one.


# Creating columns to display ascii table (Horizontal to vertical)
display_columns = int(input('Please choose numbers of columns you guys want to split table into'))

number_of_values = MAX_NUMBER - MIN_NUMBER
row_size = int(number_of_values / display_columns)
value = MIN_NUMBER

for rows in range(row_size + 1):
    for column in range(display_columns):
        print("{:>6} {:>3}".format(value, chr(value)), end=" ")
        value += 1
        if value > MAX_NUMBER:
            break
    print()


# Creating columns (vertical to horizontal)
check_value = MIN_NUMBER
for rows in range(row_size + 1):
    value = MIN_NUMBER + rows
    for column in range(display_columns):
        display_value = value + (column * row_size)
        print("{:>12} {:>5}".format(display_value, chr(display_value)), end="")
        value += 1

        check_value += 1
        if check_value > MAX_NUMBER:
            break
    print()
# Practice this. Had to slightly glance at solution. I just kept mixing up variables to use for some reason in calculations.
# Make sure to get through step by step


