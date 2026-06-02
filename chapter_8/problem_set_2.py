# 8-9

def magicians(new_magicians):
    for magician in new_magicians:
        print(magician)

new_magicians = ['Dave', 'Brian', 'Phil', 'Dumbledore']

magicians(new_magicians)

# 8-10

def great_magicians(new_magicians):
    for magician in new_magicians:
        print(magician + ' the Great')

great_magicians(new_magicians)
magicians(new_magicians)