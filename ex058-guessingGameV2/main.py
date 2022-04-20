from random import randint

num = 0
randNum = randint(1,20)
tries = 1

while num != randNum:
    num = int(input('Enter a number between 1 and 20: '))

    if num == randNum:
        print(f'Correct. The number is {num}')
        print(f'You tried {tries} times until enter the right number.')
    else:
        print('Wrong. Try again.')
        tries += 1
