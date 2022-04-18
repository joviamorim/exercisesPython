sumAge = 0
older = 0        # the age of oldest man
olderName = ''   # the name of oldest man
under20 = 0      # quantity of women under 20 years old

for i in range(0,5):
    name = input(f'Insert the name of person number {i+1}: ').strip()
    age = int(input(f'Inser the age of person number {i+1}: '))
    gender = input(f'The person {i+1} is male("m") or female("f")? ').strip()

    sumAge = sumAge + age

    if gender == 'm':
        if age > older:
            older = age
            olderName = name
    else:
        if age < 20:
            under20 += 1
    

averageAge = sumAge/5

print(f'Average age: {averageAge}')
print(f'Name of oldest man: {olderName}')
print(f'Quantity of women under 20 years old: {under20}')
