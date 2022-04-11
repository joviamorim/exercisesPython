num = int(input('Insert a number: '))

base = int(input('Choose a number base to convert:\n 1- binary\n 2- octal\n 3- hexadecimal\n'))

if base == 1:
    binary = bin(num)
    print(f'The number in binary: {binary}')
elif base == 2:
    octal = oct(num)
    print(f'The number in octal base: {octal}')
elif base == 3:
    hexadecimal = hex(num)
    print(f'The number in hexadecimal: {hexadecimal}')
else:
    print('please, choose a valid option.')
