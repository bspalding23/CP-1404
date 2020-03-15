
TARIFFS = 11, 31

tariff = int(input("Please enter what tariff you are on. 11 or 31\n"))
while tariff not in TARIFFS:
    tariff = int(input("That tariff doesn't exist. Please choose form 11 or 31\n"))

price_per_kWh_cents = 0
if tariff == 11:
    price_per_kWh_cents = 0.244618
else:
    price_per_kWh_cents = 0.136928

daily_use_kWh = float(input("Please enter daily usage in kWh\n"))

number_days = int(input("Please enter how long the billing period is\n"))

estimated_bill = price_per_kWh_cents * daily_use_kWh * number_days

print("Your estimate bill: {:.2f}".format(estimated_bill))
