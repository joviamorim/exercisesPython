students = dict()
studentsList = list()

for i in range(0,3):
    students['name'] = input("Insert your name: ")
    students['mean'] = int(input("Insert the arithmetic mean: "))
    studentsList.append(students.copy())

print(studentsList)
