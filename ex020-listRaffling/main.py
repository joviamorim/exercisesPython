import random

n1 = input('Type the name 1: ')
n2 = input('Type the name 2: ')
n3 = input('Type the name 3: ')

list = [n1,n2,n3]

random.shuffle(list)

print(f'The shuffled list is:\n{list}')
