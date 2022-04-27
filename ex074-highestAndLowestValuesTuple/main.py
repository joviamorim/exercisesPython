from random import randint

randNums = (randint(0,10),randint(0,10),randint(0,10),randint(0,10))
high = randNums[0]
low = randNums[0]

for n in randNums:
    print(f"{n} ", end="")

# two ways to do
'''for i in randNums:
    if i > high:
        high = i
    else:
        if i < low:
            low = i

print(f"\nHighest number: {high}")
print(f"Lowest number: {low}")'''

print(f'\nHighest number: {max(randNums)}')
print(f'Lowest number: {min(randNums)}')
