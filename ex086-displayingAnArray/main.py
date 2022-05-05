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
