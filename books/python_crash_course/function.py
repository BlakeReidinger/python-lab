#Defining a Function
def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

#Passing information in a Function
def greet_user(username):
    """Displays simple greeting"""
    print(f" Hello, {username.title()}!")

greet_user('jessie')

#8-1 message
def display_message():
    """Show what we have been learning this chapter"""
    print("We are learning about functions this chapter!")

display_message()

#Favorite Book
def favorite_book(title):
    """Show was my favorite book is"""
    print(f"My favorite book has got to be {title.title()}!")

favorite_book('bible')


#Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}. ")

describe_pet('hamster', 'harry')
#Multiple Fucntion Calls
describe_pet('dog', 'karma')

#Key word Arguments
def describe_pet(pet_type, pet_name):
    """Display information on the pet"""
    print(f"\nI have a {pet_type}. ")
    print(f"My {pet_type}'s name is {pet_name.title()}. ")
#The order of key word arguments does not matter
describe_pet(pet_type = 'cat', pet_name = 'tigger')

#Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='karma')
describe_pet('tigger', 'cat')


#Equivalent Function Calls
#A dog named Willie
describe_pet('willie')
describe_pet(pet_name= 'willie')

# A hamster named harry
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type= 'hamster', pet_name= 'harry')
#^^^Each of these function calls would have the same output

#8-3 T shirts
def make_shirt(size, text):
    """Summarize shirt going to be made"""
    print(f"\nIm going to make a {size} T-shirt")
    print(f"It is going to say {text}")

make_shirt('medium', 'I love coding!')


#8-4
def make_shirt(text= 'I Love Python', size= 'Large'):
    """Summerize shirt going to be made"""
    print(f"\nIm going to make a {size} T-shirt")
    print(f"\nIts going to say {text}")

make_shirt()
make_shirt(size= 'Medium')
make_shirt(size= 'small', text= 'I Figured out the error')


#8-5 Cities
def describe_city(city, location= 'East coast'):
    """Displays information on the city"""
    print(f"\n {city.title()} is in {location.title()}")

describe_city('new york city', 'new york')
describe_city(city= 'buffalo')
describe_city('jersey city')
describe_city('charolatte')


#Returning a simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('chase', 'reidinger')

print(f"\n{musician}")


#Making an argument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name neatly formatted"""
    if middle_name:
        full_name = f" {first_name} {middle_name} {last_name}"
    else:
        full_name = f" {first_name} {last_name}"
    return full_name.title()

gamer = get_formatted_name('Blake', 'Joseph')
print(gamer)

assassin = get_formatted_name('edward', 'lee', 'kenway')
print(f"\n {assassin}")

#Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

gamer = build_person('blake', 'reidinger')
print(gamer)


#Using a While loop in a function




#8-6 Citys
def city_country(name, location):
    """Show name and location of a city"""
    return f"{name.title()}, {location.title()}"

city = city_country('New York', 'United States')
print(city)
city = city_country('Sydney', 'Aulstarlia')
print(city)
city = city_country('Berlin', 'germany')
print(city)


#8-7 make album
def make_album(artist_name, album_title, tracks=0):
    """build a dictionary about arist and albums"""
    album_dict = {
    'artist': artist_name.title(),
    'album': album_title.title(),
    }
    if tracks:
        album_dict ['tracks'] = tracks
    return album_dict

album = make_album('Migos', 'Culture 2')
print(album)
album = make_album('nav', 'Brown boy 2')
print(album)
album = make_album('21 savage', 'ISSA')
print(album)
album = make_album('Linken park', 'hybrid theory', tracks = 8)
print(album)


#User albums
def make_album(artist, title, tracks=0):
    """Build a dcitionary about a album"""
    album_dict = {
    'artist': artist.title(),
    'title': title.title(),
    }
    if tracks:
        album_dict ['tracks'] = tracks
    return album_dict


#Favorite games
def favorite_games(genre, title):
    """Show what my favorite games are"""
    game_dict = {
    'genre': genre.title(),
    'title': title.title(),
    }
    return game_dict
print("\nHere are my favorite games!")

game = favorite_games('shooter', 'halo')
print(game)
game = favorite_games('action adventure', 'assassins creed')
print(game)
game = favorite_games('sports', 'madden 16')
print(game)
game = favorite_games('strategy', 'worms')
print(game)

#Passing a list
def greet_users(names):
    """Print a simple message to each user"""
    for name in names:
        msg = f"Hello {name.title()}! "
        print(msg)

usernames = ['ueki420', 'aresbr117', 'ares019', 'silver salvo']
greet_users(usernames)

#Modifying a list in a function

#start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot arm', 'SOCO bender']
completed_designs = []

#Simulate printing each design until none are left
#Move each design to completed_designs once completed
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f" Adding model {current_design.title()} ")
    completed_designs.append(current_design)

#Display all completed models
print("\nThe following models have been completed: ")
for completed_design in completed_designs:
    print(completed_design)


#8-9 Short messages
def show_message(messages):
    """Print messages in a list"""
    for message in messages:
        print(message)

messages = ['Hello there', 'How are you?', 'How goes it?']
show_message(messages)


#Sending messages
def show_messages(messages):
    """Print message in a list"""
    print('Showing all messages: ')
    for message in messages:
        print(message)



def send_messages(messages, sent_messages):
    """Print each message, then move it to sent_messages"""
    print('\nSending all messages')
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["How ya doin", "Did you punch in?", " :)"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print('\nFinal list: ')
print(messages)
print(sent_messages)


#Passing a Arbitary number in a function
def requested_toppings(*toppings):
    """Print the list of toppings that have been requested"""
    print("\nMaking your Pizza ")
    for topping in toppings:
        print(f' - {topping}')

requested_toppings('Sausage')
requested_toppings('BBQ', 'pepporoni', 'extra cheese' )


#Mixing Positional and Arbitory Arguments
def make_pizza(size,*toppings):
    """Summarize the pizza we are going to make"""
    print(f'\nMaking a {size} - inch pizza with the following toppings: ')
    for topping in toppings:
        print(f' -{topping} ')

make_pizza(16, 'BBQ')
make_pizza(18, 'pepporoni', 'ham', 'onion')


#Using Arbbitary key word arguments  ** has python perform a built in dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary using everything we need to know about a user"""
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                location = 'princeston',
                field = 'physics')
print(user_profile)

#8-12 Sandwiches
def make_sandwich(*items):
    """Summarize what is on the sandwich"""
    print('\nMaking your Sandwich!:')
    for item in items:
        print(f' - {item}')

make_sandwich('Ham')
make_sandwich('Turkey', 'Provolone')
make_sandwich('Salamy', 'PP&J', 'Roast Beef')

#8-13 Builing Me
def build_me(first, last, **user_info):
    """Describing myself in a function"""
    user_info['First name'] = first
    user_info['Last name'] = last
    return user_info

blakes_profile = build_me('Blake', 'Reidinger',
                    location = 'New jersey',
                    profession = 'Production Control',
                    hobbies = 'XBOX')

print(blakes_profile)


#8-14 Cars
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car"""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color = 'blue', tow_package=True)
print(my_outback)

my_charger = make_car('Dodge', 'charger', color = 'white', led_lights=True)
print(my_charger)


#Importing an entire Module
def make_pizza(size, *toppings):
    """Summarize the pizza we are going to make"""
    print(f"\nMaking a -{size} inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" -{topping}")


import function

function.make_pizza(16, 'mushroom')
function.make_pizza(12, 'extra cheese', 'pepporoni', 'Sausage')

#Importing specific functions
from function import make_pizza
function.make_pizza(17, 'Mushroom')
function.make_pizza(18, 'Mushrooms', 'Garlic', 'Onions')
