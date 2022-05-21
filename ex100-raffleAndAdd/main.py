from random import randint


def raffle(sizeList):
    for i in range(0,sizeList):
        numbers.append(randint(1,10))
    print(f"The number list: {numbers}")


def add(nList):
    nSum = 0
    for i in nList:
        if i%2 == 0:
            nSum = nSum + i
    print(f"Sum of pair numbers: {nSum}")


numbers = list()

raffle(randint(2,10))
add(numbers)

