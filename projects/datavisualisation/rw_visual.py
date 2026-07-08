import matplotlib.pyplot as plt
from random_walk import RandomWalk

run_number = 1

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    plt.figure()
    plt.plot(rw.x_values, rw.y_values, c=point_numbers, lw=1, edgecolors='none', s=1)
    
    filename = f"randomwalkimages/random_walk_{run_number}.png"
    plt.savefig('randomwalkimages/random_walk.png', bbox_inches='tight')

    keep_running = input("Run again? (y/n):")
    if keep_running == 'n':
        break

    run_number += 1 # Increments the run count after each successful run.