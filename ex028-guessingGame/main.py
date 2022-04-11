import random

drawnNum = random.randrange(0,6)

num = int(input('Type a number between 0 and 5: '))

if num == drawnNum:
    print(f'Correct! the number is {drawnNum}')
else:
    print(f'Wrong. The correct number is {drawnNum}')
