num = 0
sum = 0

# when the user enters a number greater than 100, the program shows the sum of all values (disregarding the flag)
while num < 100:
    num = int(input('Enter a number: '))
    if num < 100:
        sum = sum + num

print(f'The sum of values: {sum}')
