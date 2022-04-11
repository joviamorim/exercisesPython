distance = float(input('Insert the trip distance(km): '))

if distance > 200:
    kmPrice = 0.45
else:
    kmPrice = 0.50

price = distance*kmPrice

print(f'The final trip price is: {price:.2f}')
