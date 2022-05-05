students = []
infos = []
grades = []

while True:
    infos.append(input("Insert the name: "))
    grades.append(int(input("Type the grade 1: ")))
    grades.append(int(input("Type the grade 2: ")))

    infos.append(grades[:])

    mean = (grades[0]+grades[1])/2
    infos.append(mean)

    students.append(infos[:])
    infos.clear()
    grades.clear()

    add = input("Do you want to add another student? (y/n): ")
    if add == 'n':
        break

print("="*20)
print(f"{'num':<4}{'name':<10}{'mean':<4}")
for i in range(0,len(students)):
    print(f"{i:<4}{students[i][0]:<10}{students[i][2]:<4}")
print("="*20)

choose = int(input("Pick a student by their number to see their grade: "))

print(f"{students[choose][1]}")
