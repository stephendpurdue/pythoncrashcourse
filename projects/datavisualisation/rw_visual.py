import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c=point_numbers, edgecolors='none', s=1)
    plt.show()

    keep_running = input("Run again? (y/n):")
    if keep_running == 'n':
        break

plt.savefig('randomwalkimages/random_walk.png', bbox_inches='tight')