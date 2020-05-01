
from prac_06.guitar import Guitar


def main():
    guitar = Guitar("Gibson_L-5_CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1000.00)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98, guitar.get_age()))

    print("{} get_age() - Expected {}. Got {}".format(other.name, 7, other.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))

    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


main()
