gender = ''

while gender != 'm' and gender != 'f':
    gender = input('Enter your gender\n m = male\n f = female\n')

    if gender == 'm':
        print('Your gender: male')
    elif gender == 'f':
        print('Your gender: female')
    else:
        print('Please insert a valid gender.')
