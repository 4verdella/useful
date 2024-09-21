# UZS -> USD
sum_amount = float(input("Enter the amount in UZS (SUM): "))
usd_rate = float(input("Enter the exchange rate for USD (1 USD = ? UZS): "))
def convert_sum_to_usd(sum_amount, usd_rate):
    return sum_amount / usd_rate

usd_amount = convert_sum_to_usd(sum_amount, usd_rate)
print(f"{sum_amount:.2f} UZS is {usd_amount:.2f} USD")

# USD -> EURO
sum_amount = float(input("Enter the amount in UZS (SUM): "))
eur_rate = float(input("Enter the exchange rate for EUR (1 USD = ? EUR): "))


def convert_usd_to_eur(usd_amount, eur_rate):
    return usd_amount * eur_rate

# Convert USD to EUR
eur_amount = convert_usd_to_eur(usd_amount, eur_rate)
print(f"{usd_amount:.2f} USD is {eur_amount:.2f} EUR")



# EURO -> SUM 
sum_amount = float(input("Enter the amount in UZS (SUM): "))
eur_to_sum_rate = float(input("Enter the exchange rate for EUR to UZS (1 EUR = ? UZS): "))



def convert_eur_to_sum(eur_amount, eur_to_sum_rate):
    return eur_amount * eur_to_sum_rate


# Convert EUR back to SUM
final_sum_amount = convert_eur_to_sum(eur_amount, eur_to_sum_rate)
print(f"{eur_amount:.2f} EUR is {final_sum_amount:.2f} UZS")

