from random import randint

startNumbers = []
numbers = []
choosedNums = []

for i in range(1,61):
        startNumbers.append(i)

games = int(input("How many games do you want to make?  "))

for g in range(0,games):
    numbers = startNumbers[:]
    choosedNums.clear()

    for i in range(0,6):
        randNum = randint(numbers[0], numbers[-1])
        numbers.remove(randNum)
        choosedNums.append(randNum)

    choosedNums.sort()
    print(choosedNums)
