n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

if n1 > n2:
    print(f'The number {n1} is the biggest')
elif n2 > n1:
    print(f'The number {n2} is the biggest')
else:
    print(f'The numbers {n1} and {n2} are the same')
