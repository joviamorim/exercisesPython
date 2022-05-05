numList = []

'''for i in range(0,5):
    num = int(input("Type a number: "))

    if num in numList:
        print("Already existing number.")
        continue

    if numList == []:
        numList.append(num)
        print("First number added.")
    else:
        for pos,j in enumerate(numList):
            if pos == len(numList)-1:
                if num > j:
                    numList.append(num)
                    print("Number added in last position.")
                    break
                else:
                    numList.insert(pos,num)
                    print(f"Number added in position: {pos}")
                    break
            elif num < j:
                numList.insert(pos,num)
                print(f"Number added in position: {pos}")
                break'''

for i in range(0,5):
    num = int(input("Type a number: "))

    if i == 0 or num > numList[-1]:
        numList.append(num)
        print("Number added in last position.")
    else:
        pos = 0
        while pos < len(numList):
            if num == numList[pos]:
                print("Already existing number.")
            elif num < numList[pos]:
                numList.insert(pos,num)
                break
            pos+=1

print(f"All sorted numbers: {numList}")
            