from die import Die
import pygal

die_1 = Die()
die_2 = Die()
die_3 = Die()

# Roll the dice a set amount of times and store in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() * die_2.roll() * die_3.roll()
    results.append(result)

# Analyze the results

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Create a histogram

hist = pygal.Bar()

hist.title = "Results of rolling three 6 sided dice 50,000 times"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.x_labels = [x for x in range(1, 19)] # listcomp for automatically generating labels.


hist.add('D6' + 'D6' + 'D6', frequencies)
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)