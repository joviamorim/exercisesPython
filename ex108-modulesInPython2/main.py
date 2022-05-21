import currency

c = float(input("Insert the value: "))

print(f"Value with 10% discount: {currency.currency(currency.discount(c))}")
print(f"Half value: {currency.currency(currency.half(c))}")
print(f"Twice the value: {currency.currency(currency.twice(c))}")
