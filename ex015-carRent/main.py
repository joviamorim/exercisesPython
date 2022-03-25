# get the rent time (days)
t = int(input('Type the rent time in days: '))
# get the distance traveled (kilometers)
d = float(input('Type the distance traveled: '))

# diary price
tPrice = 100.5
# distance traveled price per kilometer
dPrice = 2.5

# calculating the price to pay
cost = (t*tPrice) + (d*dPrice)

print(f'Price to pay: ${cost}')
