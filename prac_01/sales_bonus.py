"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MIN_SALES_FOR_BIG_BONUS = 1000


def main():
    sales = float(input("Please enter your sales to have your bonus calculated\n"))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print("Congrats. Your bonus is {}".format(bonus))
        sales = float(input("Please enter your sales to have your bonus calculated\n"))

    print("Thank you")


def calculate_bonus(sales):
    if sales < MIN_SALES_FOR_BIG_BONUS:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    return bonus


main()
