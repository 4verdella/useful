def convert_sum_to_usd(sum_amount, usd_rate):
    return sum_amount / usd_rate

def convert_usd_to_eur(usd_amount, eur_rate):
    return usd_amount * eur_rate

def convert_eur_to_sum(eur_amount, eur_to_sum_rate):
    return eur_amount * eur_to_sum_rate

# Misol uchun valyuta kurslari:
usd_rate = 12000  # 1 USD = 12000 UZS
eur_rate = 0.85   # 1 USD = 0.85 EUR
eur_to_sum_rate = 14000  # 1 EUR = 14000 UZS

# Foydalanuvchi miqdorini kiriting (SUM)
sum_amount = 2400000

# SUM dan USD ga
usd_amount = convert_sum_to_usd(sum_amount, usd_rate)
print(f"{sum_amount} UZS is {usd_amount:.2f} USD")

# USD dan EUR ga
eur_amount = convert_usd_to_eur(usd_amount, eur_rate)
print(f"{usd_amount:.2f} USD is {eur_amount:.2f} EUR")

# EUR dan SUM ga
final_sum_amount = convert_eur_to_sum(eur_amount, eur_to_sum_rate)
print(f"{eur_amount:.2f} EUR is {final_sum_amount:.2f} UZS")