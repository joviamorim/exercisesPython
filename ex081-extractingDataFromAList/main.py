numList = []

while True:
    numList.append(int(input("Type a number: ")))
    add = input("Do you want to add another number? y=yes, n=no\n")

    if add == 'n':
        break

lenList = len(numList)
print(f"List length: {lenList}")

numList.sort(reverse=True)
print(f"List in decending order: {numList}")

if 5 not in numList:
    print("Number 5 is not on the list")
else:
    print("Number 5 is on the list")
