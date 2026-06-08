import json
# 10-11 + 10-12 + 10-13

class load():
    # Takes information and dumps it into a json file.
    @staticmethod
    def json_dump():

        words = ['Cake', 'Car', 'Truck', 'Pizza']

        wordfile = 'words.json'
        with open(wordfile, 'w') as w_obj:
            json.dump(words, w_obj)



    # Loads a json file and prints the contents
    @staticmethod
    def json_load():

        load = 'words.json'
        with open(load) as l_obj:
            words = json.load(l_obj)

        print("I know your favourite words! They are: " + str(words))
        check = print("Is this correct: ")
        if check == "yes".lower():
            print("I know!")
        else:
            new_words = input("Please enter your favourite words: ")
            words.append(new_words)

load.json_dump()
load.json_load()