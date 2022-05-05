person = []
people = []
i = 0

while True:
    person.append(input("Insert your name: "))
    person.append(float(input("Type your weight: ")))

    people.append(person[i:])
    i+=2

    add = input("Do you want to add another person? y=yes, n=no\n")

    if add == 'n':
        break

heavy = []
hWeight = person[1] # person[1] = first name on the list

light = []
lWeight = person[1] # person[1] = first name on the list

for j in range(0,len(people)):
    if people[j][1] > hWeight:
        heavy = people[j][0]
        hWeight = people[j][1]
    elif people[j][1] == hWeight:
        heavy.append(people[j][0])
        hWeight = people[j][1]
    elif people[j][1] < lWeight:
        light = people[j][0]
        lWeight = people[j][1]
    elif people[j][1] == lWeight:
        light.append(people[j][0])
        light = people[j][1]

print(people)
print(f"heaviest: {heavy}")
print(f"Lightest: {light}")
