import sys

menu = [
    { 'name': 'Magnum', 'price': 3000},
    { 'name': 'Uzi', 'price': 5000},
    { 'name': 'Striker', 'price': 7000},
    { 'name': 'Hunting Rifle', 'price': 9000},
    { 'name': 'Rocket launger', 'price':10000},
    { 'name': 'Ammo', 'price': 300},
    { 'name': 'Grenades', 'price': 500},
]

player_inv = []


def show_menu(menu):
    """Print entire menu to screen"""
    for index, item in enumerate(menu):
        print(f" {index} {item['name']} ${item['price']}")

def calc_total(inventory):
    """Calculate sum of items"""
    total = 0
    for product in inventory:

        item = menu[product]

        total = total + item['price']

    print(total)

def show_inventory(inventory):
    """show items in inventory"""
    print('inventory')
    for product in inventory:
        item = menu[product]
        print(item['name'])

def buy():
    ip = input('Enter what you need to survive \npress q to quit')
    if str(ip) == 'q':
        print('goodluck stranger')
        sys.exit()
    print(ip)
        #adds items to inventory
    player_inv.append(int(ip))
    print(f"player_inv: {player_inv}")

    show_inventory(player_inv)
    calc_total(player_inv)


def sell():
    print('im selling my shit')




show_menu(menu)

print('Welcome stranger what are ya buyin')

while True:
    ip = input('are you buying or selling stranger')
    if str(ip) == 'buy':
        buy()
    if str(ip) == 'sell':
        sell()
