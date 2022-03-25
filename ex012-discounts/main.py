# get the product price
price = float(input('Insert the price: '))
# apply the discount
percent = 5
# disc = price*percent/100
finalPrice = price - (price*percent/100)

print(f'The price with discount of {percent}%: {finalPrice}')
