numList = []
evenList = []
oddList = []

for i in range(0,5):
    numList.append(int(input("Type a number: ")))

for n in numList:
    if n%2 == 0:
        evenList.append(n)
    else:
        oddList.append(n)

print(f"All numbers: {numList}")
print(f"Even numbers: {evenList}")
print(f"Odd numbers: {oddList}")
