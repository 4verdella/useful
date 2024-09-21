from_convert = float(input("Welcome\n1)USD\n2)SUM\n3)EUR\nChoose: "))
to_convert = float(input("Convert to:\n1)USD\n2)SUM\n3)EUR\nChoose: "))
amount = float(input("Enter the amount: "))


# Conversion rates
usd = 12.700  # 1 USD to SUM
eur = 29.000  # 1 EUR to SUM

# Conversion logic
if from_convert == 1 and to_convert == 2:
    print(f"{amount * usd:.2f} SUM")
elif from_convert == 1 and to_convert == 3:
    print(f"{(amount * usd) / eur:.2f} EUR")
elif from_convert == 2 and to_convert == 1:
    print(f"{amount / usd:.2f} USD")
elif from_convert == 2 and to_convert == 3:
    print(f"{amount / eur:.2f} EUR")
elif from_convert == 3 and to_convert == 1:
    print(f"{(amount * eur) / usd:.2f} USD")
elif from_convert == 3 and to_convert == 2:
    print(f"{amount * eur:.2f} SUM")
else:
    print("You chose the wrong type!")
