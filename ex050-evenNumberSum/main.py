numSum = 0
for i in range(0,5):
    num = int(input('Enter a number: '))
    if num%2 == 0:
        numSum = num + numSum

print(f'Even numbers sum: {numSum}')
