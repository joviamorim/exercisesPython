num = int(input('Enter a number to calculate your factorial: '))

fact = 1

while num > 0:
    fact = fact * num
    num -= 1

print(f'Factorial: {fact}')
