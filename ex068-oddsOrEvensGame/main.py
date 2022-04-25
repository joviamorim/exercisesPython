from random import randint

bot = 0
sum = 0
wins = 0

while True:

    choice = input('Choose: "o"=odd, "e"=even\n')
    user = int(input('Enter a number (between 1 and 10): '))
    
    bot = randint(1,10)
    sum = user + bot   

    print(f'User: {user}, Bot: {bot}, Sum: {sum}')

    if sum%2 == 0:
        if choice == 'e':
            print('You won')
            wins += 1
        else:
            print('Yous lost')
            break
    else:
        if choice == 'o':
            print('You won')
            wins += 1
        else:
            print('You lost')
            break

print(f'Consecutive wins: {wins}')
