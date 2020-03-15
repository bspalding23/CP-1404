
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 100 + 1, 10):
    print(i, end=" ")
print()

# b.

for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c.
number_of_stars = int(input("Please enter a number\n"))
for i in range(number_of_stars):
    print("*", end=" ")
print()

# OR
stars = ""
for i in range(number_of_stars):
    stars += "* "
print(stars)

# d.
stars = ""
for i in range(number_of_stars):
    stars += "*"
    print(stars)
