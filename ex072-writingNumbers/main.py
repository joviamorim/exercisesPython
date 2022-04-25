wNumber = ("one", "two", "three", "for", "five", "six", "seven", "eight", "nine", "ten")

while True:
    num = int(input("Type a number between 1 and 10: "))

    if num >= 1 and num <= 10:
        print(wNumber[num-1])
        break
    else:
        print("This number is not between 1 and 10.")
