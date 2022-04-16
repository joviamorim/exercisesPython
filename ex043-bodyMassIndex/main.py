height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))

bmi = weight/(pow(height,2))

print(f'BMI: {bmi}')

if bmi < 18.5:
    print('Under weight')

else:
    if bmi >= 18.5 and bmi < 25:
        print('Ideal weight')
    else:
        if bmi >= 25 and bmi <= 30:
            print('Overweight')
        else:
            print('Obese')
