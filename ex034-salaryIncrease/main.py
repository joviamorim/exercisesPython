currentSalary = float(input('Type your salary: '))

if currentSalary > 1250.00:
    increase = 0.1
else:
    increase = 0.15

newSalary = currentSalary + (currentSalary*increase)

print(f'The new salary is {newSalary}')
