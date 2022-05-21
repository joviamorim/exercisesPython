import currency

c = float(input("Insert the value: "))

print(f"Value with 10% discount: {currency.discount(c, f=False)}")
print(f"Half value: {currency.half(c)}")
print(f"Twice the value: {currency.twice(c)}")
