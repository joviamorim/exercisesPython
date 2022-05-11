from random import randint
from time import sleep
from operator import itemgetter

game = {'player1': randint(1,6),
        'player2': randint(1,6),
        'player3': randint(1,6),
        'player4': randint(1,6)
        }

ranking = list()

for k, v in game.items():
    print(f"{k}: {v}")
    sleep(1)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f"Place {i+1}: {v[0]} - {v[1]}")
