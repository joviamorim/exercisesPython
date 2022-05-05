oddEven = [[],[]]

for i in range(0,7):
    num = int(input("Type a number: "))

    if num%2 == 0:
        oddEven[0].append(num)
    else:
        oddEven[1].append(num)

print(f"Even numbers: {oddEven[0]}")
print(f"Odd numbers: {oddEven[1]}")
