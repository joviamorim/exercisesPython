mValue = 0 # multiplication value

while True:
    num = int(input('Enter a number to display your multiplication table: '))

    # if the user enters a negative number, the program will terminate
    if num < 0:
        break
    else:
        for i in range(1,11):
            mValue = num*i
            print(f'{num}x{i}={mValue}')
 