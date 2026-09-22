import numpy as np
players = np.array (["sachin", "virat kohli", "yashasvi", "jaspreet", "rishab"])
matches = np.array (["ipl 25", "ipl 20", "ipl 23"])
np.random.seed(42)
runs=np.random.randint(10, 100, size=(len(players), len(matches)))
print("players", players)
print("matches", matches)
print("runs scored by each player: ")
print(runs)
