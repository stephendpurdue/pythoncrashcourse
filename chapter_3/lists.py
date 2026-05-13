# Lists are 0 indexed, meaning 'trek' would be 0.

words = ['trek', 'cannondale', 'specialized', 'cake']
print(words[1].title())

message = "My first food was " + words[3].title() + "."
print(message)


# Sort to alphabetical order.
# words.sort()
print(words)

print("Here is the original list")
print(words)

print("Here is the sorted list")
print(sorted(words))

print("Here is the original list again")
print(words)

words.reverse()
print(words)

print(len(words))