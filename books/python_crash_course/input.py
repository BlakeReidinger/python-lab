#How the input() Function works
message = input("Tell me something and I will write it back to you: ")
print(message)

#Writing Clear prompts
name = input('Please tell me your name:')
print(f"\nHello, {name}")

#prompt
prompt = "If you tell me your first name, we can peronalize the messages you see"
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")

#Using the int() to Accept Numerical Input
age = input("How old are you?")
age = int(age)
age >= 18
print(age)


height = input("How tall are you in inches?")
height = int(height)

if height > 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou need to be a little older")

#The modulo operator
number = input("Enter a number, and ill tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even!")
else:
    print(f"\nThe number {number} is odd!")


#7-1
car = input("What kind of car would you like?: ")
print(f"\nLet me see if I can find you a {car.title()}")

#7-2
group = input("How many people are you having for a dinner group: ")
group = int(group)

if group > 8:
    print("\nSorry! That is just too many people for our resteraunt")
else:
    print("\nOK! Let me reserve a table for you!")

#7-3 Multiples of 10
number = input("Tell me a number and I will say if its a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten!")
else:
    print(f"\nThe number {number} is not a multiple of ten! ")


#Using a Flag
prompt = "\nTell me something and I will repeat it backk to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#Using break to exit a loop
prompt = "\nPlease enter name of a city: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Id love to go to {city.title()}!")

#Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#7-4 Pizza toppings
prompt = "\nTell me what pizza toppings you would like?: "
prompt += "\nEnter 'quit' when you are done ordering: "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"Adding {toppings.title()} to your pizza, anything else?: ")

#7-5
prompt = "Welcome to Ace cinema, How old are you?: "
prompt += "Enter 'quit' when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print(" You get in for free!")
    elif age < 13:
            print("your ticket is $10")
    else:
        print(" Your ticket is $15. ")

#7-8 Sandwihces
sandwich_orders = ['turkey sandwich', 'PP&J', 'ham sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f" im working on your {current_sandwich} sandwich. ")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich")


#7-10
name_prompt = "\nWhats your name?"
place_prompt = "\n If you could go to one place where would you go?: "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

#Responses will be stored in the form {name: place}
responses = {}

while True:
    #Ask the user where they would like to go
    name = input(name_prompt)
    place = input(place_prompt)

#Store the response
    responses[name] = place

#Ask if there is anyone else responding
    repeat = input(continue_prompt)
    if repeat == 'no':
        break

#Show results of the survey
print("\n--- Results --- ")
for name, place in responses.items():
    print(f"{name.title()} would you like to visit {place.title()}.")
