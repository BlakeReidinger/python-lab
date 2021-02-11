#if statement example
cars = ['audi', 'bmw', 'subaru', 'toyata']
for car in cars:
    if car == 'bmw':
       print(car.upper())
    else:
      print(car.title())

#Checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

    answer = 17

    if answer != 22:
        print('That is not the right answer. Please try again!')

car = 'bmw'
print(car == 'bmw')

#Example 5-1
game = 'halo'
print("Does the game == 'Halo'? I predict True.")
print(game == 'halo')


#Simple if statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered yet?")
else:
    print("you are not old enough you fuck!")
    print("Stop being a libtard!")

#The if-elif-else Chain
age = 12
if age < 4:
    print('Your admission cost is $0')
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f" \nYour admission price is ${price}")

#Using Multiple elif Calls
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f" \nYour admission fee is ${price}")

# Omitting the else block (Not using it)
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f" \nYour admission fee is ${price}")

# Testing Multiple Conditions

requested_toppings = ['Mushrooms', 'extra cheese']

if 'Mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
    print('\nFinished making your pizza')

#Aliens Colors #1
alien_color = 'green'
if alien_color == 'green':
    print("5 points earned!")

#Aliens colors #2
alien_color = 'yellow'
if alien_color == 'green':
    print('5 points earned!')
else:
    print('10 points earned!')
#Aliens colors #3
alien_color = 'red'
if alien_color == 'green':
    print('You have earned 5 points')
elif alien_color == 'yellow':
    print('you have earned 10 points!')
else:
    print('You have earned 15 points')
#Stages of life
age = 76
if age <= 2:
    print('You are just a baby aww')
elif age < 4:
    print('You are a toddler')
elif age < 13:
    print('You are just a kid')
elif age < 20:
    print('You are just a teenager')
elif age < 65:
    print('You are a adult')
else:
    print('You are a elder')

#Favorite fruit
favorite_fruits = ['apples', 'oranges', 'peaches']
if 'apples' in favorite_fruits:
    print('Adding apples to the basket')
if 'oranges' in favorite_fruits:
    print('Adding oranges to your basket')
if 'peaches' in favorite_fruits:
    print('Adding peaches to your basket')
    print('OK your basket is all done!')

#Checking for Special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_toppings in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are all out of green peppers!")
else:
    print(f"Adding {requested_toppings}.")
print("\nFinished making your pizza sir")


#Checking that a list is not empty
requested_toppings = []
for requested_toppings in requested_toppings:
    print(f" adding {requested_toppings}.")
    print('Finished with your pizza!')

else:
    print('\nAre you sure you want a plain pizza')

#Using Multiple Lists
available_topppings = ['mushrooms', 'olives', 'green peppers',
        'pepperoni', 'pineaplle', 'extra cheese']
requested_toppings = ['mushrooms', 'extra cheese', 'french fries']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
else:
    print(f" Sorry, we do not have {requested_topping}.")
    print("\nFinished making your pizza.")


#5-8 Hello Admin
user_names = ['silver salvo', 'ueki420', 'aresbr117', 'halidoc', 'admin']
for user_name in user_names:
    if user_name == 'admin':
        print(f" Hello {user_name} would you like to see a status report?")
    else:
        print(f" Hello {user_name} thank you for logging in again")

#5-9 No users
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f" hello {username} thank you for logging in again.")

else:
    print("We need to find more users!")


#5-10 checking user_names
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f" Great, {new_user} is still available.")

#Ordinal numbers 5-11
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print('2nd')
    elif number == 3:
        print("3rd")
    else:
        print(f" {number}th")
