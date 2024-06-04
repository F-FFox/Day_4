"""
import random

import my_module
print (my_module.pi)

random_integer = random.randint(1, 5)
print (random_integer)

random_float = random.random()
print (random_float + random_integer)


Lists

Lists start with open square braket and a closing square braket. you have your items, which can be of any data type, seperated by a comma.

fruits = [item1, item2, "cherry"]


states_of_america = ["Delaware", "Pensylvania", "..."]
print(states_of_america[0])
# console will print Delaware
if you enter a negative, it will start counting from the end of the list. 

You can change entries in a list:

states_of_america[1] = "Pencilvania"

Print (states_of_america[1])
#console will print Pencilvania

Add to a list:
states_of_america.append("Pinoland")



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
"""
string = "test"
print (string[1])

