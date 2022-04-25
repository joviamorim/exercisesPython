n = 0 # number of bills of each value

cash = int(input('Insert the loot: '))

while True:

    if cash >= 50:
        n = cash//50
        cash = cash-(n*50)
        print(f'number of banknotes of 50: {n}')
    elif cash >= 20:
        n = cash//20
        cash = cash-(n*20)
        print(f'number of banknotes of 20: {n}')
    elif cash >= 10:
        n = cash//10
        cash = cash-(n*10)
        print(f'number of banknotes of 10: {n}')
    elif cash >= 1:
        n = cash//1
        cash = cash-(n*1)
        print(f'number of banknotes of 1: {n}')
    else:
        break
