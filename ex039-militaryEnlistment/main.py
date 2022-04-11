from datetime import date

currentYear = date.today().year

birth = int(input('Enter your year of birth: '))

age = currentYear - birth
enlistmentYear = birth + 18

print(f'The year of your enlistment: {enlistmentYear}')

if age < 18:
    remainingYears = 18 - age
    print(f'{remainingYears} year(s) remaining until your enlistment.')
elif age > 18:
    passedYears = age - 18
    print(f'Your enlistment was {passedYears} year(s) ago')
else:
    print('This is the year of your enlistment')
