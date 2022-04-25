tCost = 0.00 # total cost
over1000 = 0 # amount of products costing more than 1000.00
cheap = '' # name of cheapest product
cheapValue = 0.00 # cheapest product value
prod = 0 # product count

while True:
    name = input("Type the product's name: ")
    cost = float(input('Enter the value of the product: '))

    tCost += cost

    if cost > 1000.00:
        over1000 += 1
    
    prod += 1
    # first time inserting a product
    if prod == 1:
        cheap = name
        cheapValue = cost

    if cost < cheapValue:
        cheap = name
        cheapValue = cost

    cont = input('You want to finish? y=Yes, n=No\n')
    
    if cont == 'y':
        break

print(f'Total cost: {tCost}')
print(f'Number of products over 1000.00: {over1000}')
print(f'The cheapest product: {cheap}')
