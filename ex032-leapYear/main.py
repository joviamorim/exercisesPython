year = int(input('Type any year: '))

leapYear = year%4

if leapYear == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
