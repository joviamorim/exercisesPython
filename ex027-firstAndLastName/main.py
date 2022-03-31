name = input('Type your full name: ').strip()

# splitting the name and storing the length of the list 'splittedName'
splittedName = name.split()
nameCount = len(splittedName) - 1

# getting the first and last name
first = splittedName[0]
last = splittedName[nameCount]

print(f'First name: {first}')
print(f'Last name: {last}')
