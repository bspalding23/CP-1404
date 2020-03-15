
MIN_PRICE_FOR_DISCOUNT = 100
DISCOUNT = 0.10


def main():
    number_of_items = get_number_of_items()
    print("Number of items: {}".format(number_of_items))

    total_cost = get_price_of_items(number_of_items)

    if total_cost > MIN_PRICE_FOR_DISCOUNT:
        total_cost = calculate_discount(total_cost)

    print("Total price for {} items is ${:.2f}".format(number_of_items, total_cost))


def get_number_of_items():
    number_of_items = int(input("Please enter how many items you have purchased\n"))
    while number_of_items < 0:
        number_of_items = int(input("Invalid number\nPlease re-enter a valid number\n"))
    return number_of_items


def get_price_of_items(number_of_items):
    total_cost = 0
    for item in range(1, number_of_items + 1):
        price = float(input("Please enter the price for item {}\n".format(item)))
        print("Price of item {}: {:.2f}".format(item, price))
        total_cost += price
    return total_cost


def calculate_discount(total_cost):
    total_cost *= 0.9
    return total_cost


main()

# QUESTION: I run it and choose 3 items for example. Inputs were 100, 22, 45.555. Individual output was 100
# 22, 45.55. But then the total was 167.56    Why has it now rounded to .56, but didn't the step before?

# QUESTION: line 28 and 29. Would it be better like the way it's written above or this way:
#     for item in range(number_of_items):
#         price = float(input("Please enter the price for item {}\n".format(item + 1)))
