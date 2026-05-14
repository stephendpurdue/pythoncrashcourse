names = ['Brian', 'Dave', 'Phil', 'Sharon']
for name in names:
    print(name.title() + ' you are cool!')
    print(names[0:2])

# Indentation is important.

squares = []
for value in range(1,15): # Declares value in range of 1 and 15.
    square = value**3 # We want it to be to the power of 3.
    squares.append(square) # Add to the list.

print(squares) # Print new list of squares.


# The same thing but with list comprehension instead. Much simpler.

squares = [value**2 for value in range(1,11)]
print(squares)

# Tuples

measurements = (100, 25)
print(measurements[0])
print(measurements[1])