children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

my_empty_dictionary = {}
print(my_empty_dictionary)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["cheesecake"] = 8
print("After", menu)
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)


##Para agregar varias palabras clave
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

##Si quisieramos agregar 3 nuevas habitaciones, podriamos usar:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

###
# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
# print(user_ids)
# user_ids.update({"theLooper": 138475, "stringQueen": 85739})
# print(user_ids)

## Sobrescribir valores ##Sabemos que podemos agregar una clave usando la siguiente sintaxis:
menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5
print("After", menu)

## El valor "oatmeal" ha cambiado a 5.

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)


###Dict Comprehensions
##Digamos que tenemos dos listas que queremos combinar en una diccionario, como una lista de estudiantes y una lista de sus alturas
#in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#Python te permite crear un diccionario usando un dictado de comprension, con esta sintaxis:

zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)


## zip() combina dos listas en un iterador de tuplas con los elementos de la lista emparejados. Este dictado de comprensión:

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)