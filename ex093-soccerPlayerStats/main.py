stats = dict()
goals = list()
total = 0

stats['name'] = str(input("Insert the soccer player name: "))
stats['matches'] = int(input("Insert the number of matches played: "))

for i in range(0,stats['matches']):
    goals.append(int(input(f"Enter the number of goals in game {i+1}: ")))

stats['goals'] = goals.copy()

for i in range(0,len(stats['goals'])):
    total = total + stats['goals'][i]

stats['totalGoals'] = total

for k,v in stats.items():
    print(f"{k}: {v}")
