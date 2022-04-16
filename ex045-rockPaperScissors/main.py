from random import randint

# 1 = rock
# 2 = paper
# 3 = scissor
user = int(input(' 1- Rock\n 2- Paper\n 3- Scissor\n Enter a number: '))

if user == 1:
    uChoice = 'Rock'
elif user == 2:
    uChoice = 'Paper'
else:
    uChoice = "Scissor"

bot = randint(1,3)

if bot == 1:
    bChoice = 'Rock'
elif bot == 2:
    bChoice = 'Paper'
else:
    bChoice = "Scissor"

print(f'user: {uChoice}, bot: {bChoice}')
if user == bot:
    print('Draw')
else:
    if user == 1:
        if bot == 2:
            print('You lost')
        else:
            print('You win')
    elif user == 2:
        if bot == 3:
            print('You lost')
        else:
            print('You win')
    else:
        if bot == 1:
            print('You lost')
        else:
            print('You win')
