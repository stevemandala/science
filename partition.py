import random
import numpy

num_players = 100
num_dollars = 100

# Returns the simulation of the n players, k dollar game
current_dist = num_players * [num_dollars]
for iter in range(0, 1000):
  for player in range(0, len(current_dist)):
    if (current_dist[player] == 0): continue
    current_dist[player] -= 1
    recipient = (int)(random.random() * num_players)
    current_dist[recipient] += 1

print("Results of the run")
print(current_dist)
print("Mean: "+ str(numpy.mean(current_dist)))
     
