# get name
name = input('Insert your name: ').strip()

# name in upper and lower case
up = name.upper()
lw = name.lower()

# analyzing the name length
# counting the spaces in string
spaces = name.count(' ')
# quantity of letters in name
le = len(name) - spaces

# getting the first name
fn = name.split()
# quantity of letters in first name
fnle = len(fn[0])

# getting the first name length using find()
# fnle = nome.find(' ') <-- this will give you the position of first space in name, that is the first name length

# displaying the results
print('Analyzing your name.')
print(f'Your name in upper case: {up}')
print(f'Your name in lower case: {lw}')
print(f'Your name have {le} letters')
print(f'Your first name is {fn[0]} and have {fnle} letters')
