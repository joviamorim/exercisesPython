phrase = input('Say something: ').strip()

phrase = phrase.lower()
letter = phrase[0]
lastLetter = phrase.rfind(letter) + 1
letterCount = phrase.count(letter)

print(f'This phrase has {letterCount} letters {letter}.')
print(f'The last {letter} appears in position {lastLetter}.')
