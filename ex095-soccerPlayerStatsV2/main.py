stats = dict()
goals = list()
players = list()
total = 0

while True:
    stats.clear()
    goals.clear()
    total = 0
    stats['name'] = str(input("Insert the soccer player name: "))
    matches = int(input("Insert the number of matches played: "))

    for i in range(0,matches):
        goals.append(int(input(f"Enter the number of goals in game {i+1}: ")))

    stats['goals'] = goals.copy()

    for i in range(0,len(stats['goals'])):
        total = total + stats['goals'][i]

    stats['totalGoals'] = total

    players.append(stats.copy())

    add = str(input("Do you want to add another player? [y/n]: "))
    if add == 'n':
        break

print(f"{'code':<5}{'name':<15}{'goals':<15}{'total':<15}")
print("-"*40)
for k,v in enumerate(players):
    print(f"{k:<5}", end='')
    for s in v.values():
        print(f"{str(s):<15}", end='')
    print("\n")
print("-"*40)

while True:
    search = int(input("Enter the code of the player you want to find (999 ends): "))

    if search == 999:
        break
    elif search >= len(players):
        print("Code not found. Try again")
    else:
        print(f"{'code':<5}{'name':<15}{'goals':<15}{'total':<15}")
        print("-"*40)
        p = players[search]
        print(f"{search:<5}{p['name']:<15}{p['goals']:<15}{p['totalGoals']:<15}")
        print("-"*40)

    add = str(input("Do you want to search another player? [y/n]: "))
    if add == 'n':
        break
