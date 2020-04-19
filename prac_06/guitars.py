
from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Please enter guitar name:\n")
    while name != "":
        year = int(input("Please enter Year:\n"))
        cost = float(input("Please enter the cost:\n$"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        print(guitars)
        name = input("Please enter guitar name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("Here are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {:>30} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                       vintage_string))
    else:
        print("Sorry you have no guitars")


main()
