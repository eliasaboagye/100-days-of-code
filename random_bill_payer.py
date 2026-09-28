import random

#get list of names separated by a comma
names = input("Input names separated by a comma and a space: \n")

list_names = names.split(", ")# separate the list to get names
random_index = random.randint(0, len(list_names)-1)

print(f"\n{list_names[random_index]} is going to buy the meal today")
