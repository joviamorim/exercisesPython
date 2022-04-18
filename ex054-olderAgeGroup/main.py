older = 0 # number of people over 18 years old
under = 0 # under 18 years old

for i in range(0,5):
    age = int(input(f'Enter the age of person number {i+1}: '))

    if age >= 18:
        older += 1
    else:
        under += 1

print(f'Number of people over 18 years: {older}')
print(f'Number of people under 18 years: {under}')
