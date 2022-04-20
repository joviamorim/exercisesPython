option = 0

while option != 5:

    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))

    print('Menu:')
    option = int(input(' 1- Sum\n 2- Multiplication\n 3- Highest number\n 4-Choose other numbers\n 5-Exit\n'))

    if option == 1:
        sum = n1+n2
        print(f'Sum: {sum}')
    elif option == 2:
        mult = n1*n2
        print(f'Multiplication: {mult}')
    elif option == 3:
        if n1 == n2:
            print('Same number')
        else:
            if n1 > n2:
                print(f'Highest number: {n1}')
            else:
                print(f'Highest number: {n2}')
    elif option == 4:
        print('Choose other numbers:')
    elif option == 5:
        exit()
    else:
        print('Enter a valid option')
