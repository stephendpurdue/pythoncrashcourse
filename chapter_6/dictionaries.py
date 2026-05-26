score = {'colour': 'blue', 'points': 5}

print(score['colour'])
print(score['points'])

# Adding to an existing dictionary.


score['x_position'] = 0
score['y_position'] = 25

# Access the key-value pair in the dictionary.

new_score = score['points']
print("You just earned " + str(new_score) + " points!")


print(score)

# Starting with an empty dictionary

cake = {'shape': 'round'}
print("The shape of the cake is " + cake['shape'] + ".")

cake['shape'] = 'square'
print("The shape of the cake is now " + cake['shape'] + ".")

cake['flavour'] = 'chocolate'
print(cake)

# Modifying values in a dictionary

