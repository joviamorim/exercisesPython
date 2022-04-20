num = 0
numCount = 0
mean = 0
high = 0
low = 0
cont = True # cont = continue

# while cont is True, the program will continue to ask numbers
while cont == True:
    num = int(input('Enter a number: '))
    numCount += 1

    # If user is entering the first number, the program defines mean = num, high = num, low = num
    if numCount >= 2:
        mean = (mean + num)/2
    else:
        mean = num
        high = num
        low = num

    if num > high:
        high = num  
    elif num < low:
        low = num

    choose = input('You want to continue? "y" = Yes, "n" = No. ')

    if choose == 'y':
        cont = True
    else:
        cont = False

print(f'Highest number: {high}')
print(f'Lowest number: {low}')
print(f'Arithmetic mean: {mean}')
