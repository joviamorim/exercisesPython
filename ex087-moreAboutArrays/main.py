array = []
matrix = []

for i in range(0,3):
    for j in range(0,3):
        array.append(int(input(f"Type the number in {i},{j}: ")))
    matrix.append(array[:])
    array.clear()

print("=+"*10)

for i in matrix:
    print(i)

print("=+"*10)

# sum of even number
numSum = 0
for i in matrix:
    for j in i:
        if j%2==0:
            numSum = numSum+j

# sum of numbers in column 3
columnSum = 0
for i in matrix:
    columnSum = columnSum+i[2]

# highest number in line 2
high = matrix[1][0]
for i in matrix[1]:
    if i > high:
        high = i

print(f"Sum of even numbers: {numSum}")
print(f"Sum of numbers in column 3: {columnSum}")
print(f"Highest number in line 2: {high}")
