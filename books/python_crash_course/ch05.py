animals = ['man', 'bear', 'pig']
print(animals[0])
print(animals[1])
print(animals[2])

animals = ['man', 'bear', 'pig']
print(animals[0])
animals[0] = 'cat'
print(animals[0])

animals = ['man', 'bear', 'pig']
animals.extend(['cow', 'duck'])
print(animals)

more_animals = ['horse', 'dog']
animals.extend (more_animals)
print(animals)

part_of_a_horse = 'horse'[1:3]
print(part_of_a_horse)

animals = ['man', 'bear', 'pig']
bear_index = animals.index('bear')
print(bear_index)

animals = ['man', 'bear', 'pig']
for animal in animals:
    print(animal.upper())

for number in range(3):
    print(number)

to_do_list = []
finished = False
while not finished:
    task = input('Enter a task for your to-do list. Press <enter> when done:')
    if len(task) == 0:
        finished = True
    else:
        to_do_list.append(task)
        print('Task added.')

print()
print('Your To-Do List:')
print('-' * 16)
for task in to_do_list:
    print(task)
