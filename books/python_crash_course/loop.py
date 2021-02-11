magicians = ['fire', 'ice', 'lighting']
for magician in magicians:
    print(magician)

dogs = ['earl', 'fred', 'brad']
for dog in dogs:
    print(f" {dog.title()}, that was a good trick")
    print(f" i cannot wait to see youre next trick! {dog.title()}.\n")

#Doing Something after a for loop(it must not be indented)
print('Thank you to everyone that was a good show')

pizzas = ['sausage', 'pepporoni', 'BBQ']
for pizza in pizzas:
    print(f" I really like {pizza.title()}!\n")
print('I really love pizza !')

animals = ['lions', 'tigers', 'bears']
for animal in animals:
    print(animal)
    print(f" All of these {animal.title()} are dangerous\n")

print("they are all predetors !")

#Making Numerical Lists
for value in range(1, 6):
    print(value)
# the Rnage() function will always be off by one
for value in range(6):
    print(value)

#using range to make a List
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    sqaure = value ** 2
    squares.append(sqaure)
print(squares)


#Simple statistics with a list of Numbers
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

#List Comprehensions
sqaures = [value**2 for value in range(1, 11)]
print(sqaures)


for value in range(1, 21):
    print(value)
numbers = list(range(1, 21))
print(numbers)

numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for value in range(1,20,3):
    print(value)

threes = list(range(3, 31, 3))
for number in threes:
    print(number)

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

#Working with part of a List
players = ['charles', 'pete', 'humpage', 'rose', 'bowers']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[4:])
print(players[-4:])

print("Here is the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Copying a List
favorite_games = ['halo', 'call of duty', 'gears', 'madden']
friends_favorite = favorite_games[:]
favorite_games.append('NHL')
friends_favorite.append('NBA')
print('My favorite games are:')
print(favorite_games)
print("\nMy friends favorite games are:")
print(friends_favorite)

role_playing = ['Final fantasy', 'AC Odyssey', 'origins', 'anthem', 'Division']
print("The fist three items in the list are:")
print(role_playing[:3])
print("the three items in the middle are:")
print(role_playing[1:3])
print("The last three items in the list are:")
print(role_playing[-3:])
friends_rpgs = role_playing[:]
friends_rpgs.append('Borderlands')
role_playing.append('Dark souls')
print(role_playing)
print(friends_rpgs)
print("My favorite RPGS are:")
for game in role_playing:
    print(f" - {game}")
print("My friends favorite RPGS are:")
for game in friends_rpgs:
    print(f" -{game}")


#Tuples use parentheses instead of brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Looping through a Tuple
dimensions = (300, 75)
for dimension in dimensions:
    print(dimension)

#Writing over a Tuple
numbers = (200, 67)
print("Here are the original numbers")
for number in numbers:
    print(number)
numbers = (400, 100)
print("\nHere are the modified numbers")
for number in numbers:
    print(number)

#Buffet
menu_items = ('Chicken', 'Broccli', 'Rice', 'Sushi', 'Shrimp')
print("These are our only foods we have:")
for item in menu_items:
    print(f" - {item}")
menu_items = ('Chicken', 'Broccli', 'Sushi', 'beans', 'tacos')
print("our menu items have changed!")
for item in menu_items:
    print(f" - {item}")
