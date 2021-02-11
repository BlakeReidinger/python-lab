# concat example
str1 = 'potions'
str2 = 'weapons'
str3 = 'misc'

# print('My inventory contains ' + str1 + ' ' + str2 +  ' ' + str3)
# print('My inventory contains {} {} {}'.format(str1, str2, str3))


str1 = 'apples'
str2 = 'pears'
str3 = 'oranges'
print(f'My inventory contains {str1} {str2} {str3}')

print()

# arguments example
def inventory(item1, item2):
    """Print out the inventory to the screen
    args:
        item1 = some item in inventory
        item2 = some other item in inventory
    """

    print(f'inventory: {item1} {item2}')


inventory(str1, str3)

num1 = 56
str_num1 = str(num1)
print(type(num1))
print(type(str_num1))

num2 = 88
num3 = 99

summ = num2 + num3

print(summ)
#
#fuction that takes 3 argumets 1 = name 2 = INT 3= int make fuction that show stats

def show_stats(health,magic,name):
    """Shows player stats
    args:
        health: shows player health
        magic: shows player magic points
        name: the players name
    """
    print(f'name: {name}, magic: {magic}, health: {health}')


def do_attack_self(health, name):
    """Attacks the player
    args:
        health: shows player health
        name: the players name
    """

    attack = 10
    output = health - attack

    print(f'{name} health: {output}')
    return output


show_stats(magic=100, health=98, name='blake')

health = 100
health = do_attack_self(health, 'blake')
health = do_attack_self(health, 'blake')


def do_level_up(skill,level):
    """Levels the player
    args:
        skill: shows player skill
        level: shows players level
    """

    # increase level by one point
    level_increase = 1
    # increase skill  by 10 points
    skill_increase = 10

    level_up = level + level_increase
    skill_up = skill + skill_increase

    print(f'Level up: {level_up}')
    print(f'skill_up: {skill_up}')
    return

do_level_up(skill=26, level=78)
do_level_up(skill=25, level=6)
do_level_up(skill=57, level=69)
do_level_up(skill=69, level=69)
do_level_up(skill=69, level=69)
do_level_up(skill=69, level=69)
