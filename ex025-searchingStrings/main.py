userName = input('Type your full name: ').strip()

userName = userName.lower()
savedName = 'silva'

print(f'Your name have {savedName}? {savedName in userName}')
