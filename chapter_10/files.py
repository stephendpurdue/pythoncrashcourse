import json

# READING FILES
# Normal method

with open('files/info.txt') as file_object: # Locates the file and defines it as a file_object
    contents = file_object.read() # Sets the object to a variable and reads it
    print(contents.rstrip()) # Prints the read variable and removes any whitespace

# Alternative method (assign the text file a variable and use that)

filename = 'files/info.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a list of lines from a file

filename_2 = 'files/info.txt'

with open(filename_2) as file_object:
    lines = file_object.readlines() # Stores the lines in a list

for line in lines:
    print(line.rstrip()) # Prints and then removes whitespace
    print(line.strip()) 

# WRITING FILES

filename_3 = 'files/info.txt'

with open(filename_3, 'w') as f: # Open the file in 'write' mode
    f.write('I love Escape from Tarkov.\n') # Add a new line to it
    f.write('I also love Marathon.\n')


def file_checker(new_file):
    try:
        with open(new_file) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + new_file + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + new_file + " has about " + str(num_words) + " words.")

new_file = 'files/guest_book.txt'
file_checker(new_file)

# Takes information and dumps it into a json file.
def json_dump():

    words = ['Cake', 'Car', 'Truck', 'Pizza']

    wordfile = 'words.json'
    with open(wordfile, 'w') as w_obj:
        json.dump(words, w_obj)

json_dump()


# Loads a json file and prints the contents
def json_load():

    load = 'words.json'
    with open(load) as l_obj:
        words = json.load(l_obj)

    print(words)

json_load()