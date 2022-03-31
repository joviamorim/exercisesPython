savedName = 'joao'
nameLen = len(savedName)

userName = input('Your name: ').strip()

# verifying name
userName = userName.lower()
verify = userName[:nameLen] == savedName # if name == joao --> true, else --> false

print(f'Your name starts with "{savedName}"? {verify}')
