phrase = input('Enter a phrase to verify if it is a palindrome: ').strip()

# sPhrase = splited phrase, this will delete all spaces
sPhrase = phrase.split()
# fPhrase = final phrase
fPhrase = ''

# The algorithm below will join the words that was splitted
for p in range(0,len(sPhrase)):
    fPhrase = fPhrase + sPhrase[p]
# This function below do the same thing:
# joinPhrase = ''.join(sPhrase)

# length of phrase
lenPhrase = len(fPhrase)

# verifying if it is a palindrome
for i in range(0,lenPhrase):
    if fPhrase[i] != fPhrase[lenPhrase-1-i]:
        print('This phrase is not a palindrome')
        exit()

print(f'"{phrase}" is a palindrome.')
