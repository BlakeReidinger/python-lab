#Dictionary example
alien_o = {'color': 'green','points': 5}
print(alien_o['color'])
print(alien_o['points'])

#Working with dictionaries
new_points = alien_o['points']
print(f"You just earned {new_points} points!")


#Adding New Key-Value Pairs
alien_o = {'color': 'green', 'points': 5}
print(alien_o)
alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)

#Starting with an empty Dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)


#Modifying Values in a Dictionary
alien_1 = {'color': 'green'}
print(f"The alien is {alien_1['color']}")
alien_1['color'] = 'yellow'
print(f"The alien is now {alien_1['color']}.")

alien_1 = {'x_position': 0, 'y position': 25, 'speed': 'fast'}
print(f" Original position: {alien_1['x_position']}")

#Move alien to the right
#Determine how far to move the alien based on its current speed.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the x_increment
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position: {alien_1['x_position']}")


#Removing Key - Value Pairs, Note: this removes it permantaly
alien_1 = {'color': 'green', 'points': 5}
print(alien_1)

del alien_1['points']
print(alien_1)

# A  dictionary of similar objects
favorite_languages = {
'jen': 'pyhton',
'sarah': 'c',
'edward': 'ruby',
'phil': 'pyhton',
}
#Using the Dictionary
language = favorite_languages['sarah'].title()
print(f"Sarahs favorite coding language is {language}")

#Using get () to Access Values
alien_1 = {'color': 'green', 'speed': 'slow'}
point_value = alien_1.get('points', 'No point value assigned.')
print(point_value)


#Person 6-1
person = {'name': 'Mason', 'last name': 'niemi', 'age': 67, 'city':
'illiois'}
print(person)

#Favorite #
favorite_numbers = {
'blake': 1,
'savannah': 2,
'chase': 3,
'TJ': 4,
'Dante': 5,
}

num = favorite_numbers['blake']
print(f" blakes favorite number is {num}")
num = favorite_numbers['savannah']
print(f" savannahs favorite number is {num}")
num = favorite_numbers['chase']
print(f"Chases favorite number is {num}")
num = favorite_numbers['TJ']
print(f"Tjs favorite number is {num}")
num = favorite_numbers['Dante']
print(f"Dantes favorite number is {num}")

glossary = {
'string': 'A series of charcters',
'comment': 'A note in python to know what your doing',
'list': 'A collection of items in a particular order',
'loop': 'Work through a collection of items, one at a time',
'dictionary': 'A collecion of key-value pairs.',
}


#Making a glossary and presenting what each definition means in a sentance
word = 'string'
print(f"{word.title()} : {glossary[word]}")
word = 'comment'
print(f"{word.title()} : {glossary[word]}")
word = 'list'
print(f"{word.title()} : {glossary[word]}")
word = 'loop'
print(f"{word.title()} : {glossary[word]}")
word = 'dictionary'
print(f"{word.title()} : {glossary[word]}")


#Looping through a Dictionary
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#Looping through all the keys in a Dictionary
favorite_languages = {
'jen': 'python',
'sara': 'c',
'edward': 'ruby',
'phil': 'python'
}

for name in favorite_languages.keys():
    print(name.title())
if 'erin' not in favorite_languages.keys():
    print('Erin please take your poll!')

#Looping through a dctionarys keys in a particular order
favorite_languages = {
'jen': 'python',
'sara': 'c',
'edward': 'ruby',
'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()} thank you for taking the poll!')
#sorted() will print your list in alphabetical order

#Looping through a Values in a dictionary
favorite_languages = {
'jen': 'pyhton',
'sara': 'ruby',
'edward': 'ruby',
'phil': 'python'
}

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
#Set() will not print items that have been repeated in a dictionary

#Glossary 2 6-4
glossary = {
'string': 'A series of charcters',
'comment': 'A note in a program that the python interpreter ignores',
'list': 'A collection of items in a particular order',
'loop': 'Work through a collection of items, one at a time',
'dictionary': 'A collection of key-value pairs',
'key': 'The first item in a key-value pair in a dictionary',
'value': 'An item associated with a key in a dictionary',
'conditional test': 'A comparison between two values',
'float': 'A numerical value with a decimal componet',
'boolean expression': 'An expression that evaluates True or False'
}

for word, definition in glossary.items():
    print(f" {word.title()} : {definition}")

#6-5 Rivers
rivers = {
'niles': 'egypt',
'deleware': 'USA',
'fraser': 'canada',
'kuskokwim': 'alaska',
'yangtze': 'china'
}
for river, country in rivers.items():
    print(f" The {river.title()} river runs through {country.title()}")
print('\nThe following rivers are included in the data set:')
for river in rivers.keys():
    print(river.title())
print('\nThe following countrys are included in the data set')
for country in rivers.values():
    print(country.title())

#Polling 6-5
favorite_languages = {
'jen': 'python',
'sara': 'c++',
'edward': 'ruby',
'phil': 'python'
}

coders = ['phil', 'josh', 'david', 'becca', 'sara', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"\n Thank you for taking the poll {coder.title()}")
    else:
        print(f"{coder.title()} what is your favorite programming language")

#A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 10}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


#Make a empty list for storing Aliens
aliens = []

#Make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
    print("...")

#Show how many aliens you have created
print(f" Total number of aliens: {len(aliens)}")


pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese']
}
#Summerize the order
print(f"You ordered a {pizza['crust']}-crust pizza"
    " with the following toppings:")

for toppings in pizza['toppings']:
    print(f"\t{toppings}")


#A Dictionary inside a dictionary
users = {
'aeinstein': {
'first': 'albert',
'last': 'einsteien',
'location': 'princeton',
},

'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
 },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


#6-7 People
#make a empty list to store people in
people = []

#Define some people, and add them to a list
person = {
'first_name': 'eric',
'last_name': 'matthes',
'age': 46,
'city': 'sitika',
}
people.append(person)

person = {
    'first_name': 'lenny',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitika',
}
people.append(person)

person = {
'first_name': 'willie',
'last_name': 'matthes',
'age': 11,
'city': 'new york',
}
people.append(person)

#Display all of the inforamtion in the dictionary
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city} is {age} years old")


#6-8 pets
pets = []

animal = {
'animal type': 'shark',
'owner': 'aqua man',
'name': 'gitza',
'weight': 576,
'eats': 'people'
}

pets.append(animal)

animal = {
'animal type': 'gorilla',
'owner': 'nobody',
'name': 'king kong',
'eats': 'dinosours',
'weight': 3456,
}
pets.append(animal)

animal = {
'animal type': 'dog',
'owner': 'Blake',
'name': 'karma',
'weight': 46,
'eats': 'bones'
}
pets.append(animal)

#Display information about animal
for animal in pets:
    print(f"\nHeres what I know about {animal['name'].title()}")
    for key, value in animal.items():
        print(f"\t{key}: {value}")

#6-9 Favorite Places

favorite_places = {
'Blake': ['Texas', 'georgia', 'california'],
'Savannah': ['new jersey', 'wildwood', 'Miami'],
'chase': ['beach', 'aulstralia', 'blairstown']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places")
    for place in favorite_places.items():
        print(f"- {place}")

#favorite numbers
favorite_numbers = {
'mandy': [42, 17],
'micah': [46, 18, 89],
'chase': [47, 80],
}

for name,numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"- {number}")

#Cities
cites = {
    'los angeles': {
    'state': 'california',
    'population': 5000000,
    'terrain': 'moountains',
    },
    'chicago': {
    'state': 'Illios',
    'population': 3000000,
    'terrain': 'snow',
    },
    'new york city': {
    'state': 'new york',
    'population': 12000000,
    'terrain': 'flat',
    }
}

for city,city_info in cites.items():
    state = city_info['state'].title()
    population = city_info['population']
    terrain = city_info['terrain'].title()

    print(f"\n{city.title()} is in {state}")
    print(f" It has a population of {population}")
    print(f" there is alot of {terrain} terrain")
