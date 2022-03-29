import random

n1 = input('Type the name 1: ')
n2 = input('Type the name 2: ')
n3 = input('type the name 4: ')

list = [n1,n2,n3]

chosen = random.choice(list)
print(f'The name chosen was: {chosen}')
