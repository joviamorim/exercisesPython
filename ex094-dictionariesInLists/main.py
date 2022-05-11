infos = dict()
people = list()
women = list()
overAge = list()

while True:
    infos.clear()
    infos['name'] = str(input("Enter the name: "))
    infos['gender'] = str(input("Enter the gender [m/f]: "))
    infos['age'] = int(input("Enter the age: "))

    people.append(infos.copy())

    while True:
        add = str(input("Do you want to continue? [y/n]"))
        if add == 'y':
            break
        elif add == 'n':
            break
        else:
            print("Enter a valid option.")

    if add == 'n':
        break
print(people)
registeredPeople = len(people)

sumAge = 0
for i in people:
    sumAge += i['age']
meanAge = sumAge/len(people)

for i in range(0,len(people)):
    if people[i]['gender'] == 'f':
        women.append(people[i]['name'])

for i in people:
    if i['age'] >= meanAge:
        overAge.append(i['name'])

print(f"Registered people: {registeredPeople}")
print(f"Average age: {meanAge}")
print(f"List of women: {women}")
print(f"List of people over the average: {overAge}")
