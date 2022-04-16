# p = price
p = float(input('Enter the price to be paid: '))
#op option
print(r'Enter the option to pay:')
print(r'1- In cash: 10% off')
print('-----------------------')
print('Payment in installments:')
print(r'2- until 3x: 5% off')
print('3- until 5x: normal price')
print(r'4- until 10x: 5% interest')

op = int(input('Enter the option: '))

# fp = final price
if op == 1:
    fp = p - (p*0.1)

elif op == 2:
    fp = p - (p*0.05)

elif op == 3:
    fp = p

elif op == 4:
    fp = p + (p*0.05)

else:
    print('Enter a valid option.')
    exit()

print(f'Final price: {fp}')
