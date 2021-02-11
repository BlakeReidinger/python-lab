favorite_games = [ 'halo', 'gears', 'COD', 'Madden', 'Resident evil']
print(favorite_games)

#Picking a item from a list neatly
#Index positions start at 0 not 1
print(favorite_games[0].title())
print(favorite_games[1])
print(favorite_games[4].title())

# getting last item from a list
print(favorite_games[-1].title())

#Using Values from a list
message = (f" \nMy first xbox game was {favorite_games[0].title()}")
print(message)

names = [ 'mike', 'torrel', 'justin', 'tim']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

message = (f" Greetings {names[0].title()}! you should try python")
print(message)
msg = (f" Hello {names[1].title()}")
print(msg)
msg = (f" Hello {names[2].title()}")
print(msg)
msg = (f" \nHello {names[3].title()}")
print(msg)

cars = [ 'PT Cruiser', 'Lambo', 'Charger']
print(f" {cars[0]} is such a shit car")
print(f" Right now i drive a {cars[2]} its pretty rad")
print(f" My dream car would be a {cars[1].title()}, maybe one day")

# Modifying elements in a list
cars[2] = 'Corvette'
print(cars)


# Adding Elements to a list
# The simpilist way to add a new element to your list is to append them

cars.append('Ferrari')
print(cars)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#inserting items to a list

cars.insert(0, 'harley')
print(cars)

#Deleting items from a list
del cars[0]
print(cars)
del cars[1]
print(cars)

#Removing an item using the POP method
popped_cars = cars.pop()
print(cars)
print(popped_cars)

last_owned = cars.pop()
print(f" The last car that i owned was {last_owned.title()}.")
#Popping with a index
school = ['books', 'desks', 'teachers',]
popped_school = school.pop(2)
print(school)
print(popped_school)


#Removing an item by Value
halo = ['chief', 'grunts', 'elites', 'brutes',]
print(halo)
halo.remove('brutes')
print(halo)

too_annoying = 'grunts'
halo.remove(too_annoying)
print(halo)
print(f" I swear these stupid fucking {too_annoying.title()} throw so many grenades")

#Guest lists & Sending invites
siblings = ['Chase', 'TJ', 'Savannah']
name = siblings[0]
print(f" Hey {name} can you come to dinner")
name = siblings[1]
print(f" Hey {name} can you come to dinner")
name = siblings[2]
print(f" Hey {name} can you come to dinner")
print(' See you all there!')

#Channging the lists
print(f" So {siblings[2]} can not make it")
siblings[2] = 'Mom'
print(f" {siblings[2]} is going to come instead")

siblings.insert(0, 'Dad')
siblings.insert(2, 'Savannah')
siblings.append('Dante')
print(siblings)
print(f" hey {siblings[0]} see you at dinner?")
print('We have a bigger table now, more guests coming in!')
print(f" {siblings[2]} please come to dinner")
print(f" {siblings[5]} please come to dinner")
print('Sorry guys!, we only have room for two guests now.')
name = siblings.pop()
print(F" Sorry {name.title()} there is no more room")
name = siblings.pop()
print(f" Sorry {name} there is no more room at the table")
name = siblings.pop()
print( f" Sorry {name} there is no more room at the table")
name = siblings.pop()
print(f" Sorry {name}there is no more room at this table")

name = siblings[0].title()
print(f" {name} you can come to dinner")
name = siblings[1].title()
print(f" {name} you can come as well")
print(f" Sorry guys! see you there {siblings[0]} {siblings[1]} lol")
del(siblings[0])
del(siblings[0])
print(siblings)


#sorting a list permanently with the sort() method
halo = ['ghosts', 'warthog', 'mongoose', 'wraith', 'scropian']
halo.sort()
print(halo)

halo.sort(reverse = True)
print(halo)

#Sorting a list temporarily
print(' Here is the orginal List')
print(halo)
print("\nHere is the sorted List")
print(sorted(halo))
print("\nHere is the original List again")
print(halo)

gears = ['locust', 'marcus', 'dom', 'cole', 'anya', 'baird']
print(gears)
gears.reverse()
print(gears)
print(len(gears))

places = ['mexico', 'costa Rico', 'germany', 'italy', 'japan',]
print(places)
places.sort()
print("here is the sorted order")
print(places)
print("here is the reverse order")
print(sorted(places, reverse = True))
print("\nOriginal order")
print(places)
places.reverse()
print(places)
print("\nOriginal Order")
places.reverse()
print(places)
places.sort()
print(" Alphabetical order")
print(places)
places.sort(reverse = True)
print("Alphabetical order reversed")
print(places)

print(len(siblings))
#finding item at the end of a list
print(places[-1])
