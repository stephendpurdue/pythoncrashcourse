import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=12)
plt.show()

plt.savefig('randomwalkimages/random_walk.png', bbox_inches='tight')