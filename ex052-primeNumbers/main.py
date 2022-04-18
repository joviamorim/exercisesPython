num = int(input('Enter a number to verify if it is prime number: '))

# This variable will count the quantity of divisible numbers (With exception of number 1 and the inserted number)
divNumber = 0

for i in range(2,num):
    if num%2 == 0:
        divNumber += 1

if divNumber != 0:
    print(f'{num} is not a prime number.')
else:
    print(f'{num} is a prime number.')
