over18 = 0 # number of people over 18 years old
men = 0 # number of registered men
wUnder20 = 0 # number of women under 20 years old

while True:
    age = int(input('Type the age: '))
    gender = input('Type the gender (m=male, f=female)\n')

    if age >= 18:
        over18 += 1
    
    if gender == 'm':
        men += 1
    elif gender == 'f':
        if age < 20:
            wUnder20 += 1
    
    cont = input('You want to finish? (y=Yes, n=No)\n')

    if cont == 'y':
        break

print(f'Number of people over 18 years old: {over18}')
print(f'Number of registered men: {men}')
print(f'Number of women under 20 years old: {wUnder20}')
