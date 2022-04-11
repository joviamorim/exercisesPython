n1 = float(input('Type the first number: '))
n2 = float(input('Type the second number: '))
n3 = float(input('Type the third number: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} is the highest number ')
    if n2 > n3:
        print(f'{n3} is the smallest number')
    else:
        print(f'{n2} is the smallest number')
else:
    if n2 > n3:
        print(f'{n2} is the highest number ')
        if n1 > n3:
            print(f'{n3} is the smallest number')
        else:
            print(f'{n1} is the smallest number')
    else:
        print(f'{n3} is the highest number ')
        if n1 > n2:
            print(f'{n2} is the smallest number')
        else:
            print(f'{n1} is the smallest number')
