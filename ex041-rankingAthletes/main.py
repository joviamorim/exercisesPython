from datetime import date

y = int(input('Enter your birth year: '))

# cY = current year
cY = date.today().year

age = cY - y

if age <= 9:
    print(f'{age} years: Child athlete')
else:
    if age > 9 and age <= 14:
        print(f'{age} years: Infant athlete')
    else:
        if age > 14 and age <= 19:
            print(f'{age} years: Junior athlete')
        else:
            if age > 19 and age <= 20:
                print(f'{age} years: Senior athlete')
            else:
                print(f'{age} years: Master athlete')
