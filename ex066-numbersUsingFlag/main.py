sum = 0

while True:
    num = int(input('Enter a number: '))

    if num > 100:
        break
    sum += num

print(f'Sum of values (disregarding the last number): {sum}')
