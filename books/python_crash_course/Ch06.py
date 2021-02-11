import sys

menu = [
    { 'name': 'ice cream', 'price': 3.50},
    { 'name': 'brownie', 'price': 4.00},
    { 'name': 'cookie', 'price': 2.00}
]

customer_orders = []

def show_menu(menu):
    """ print entire menu to screen"""
    for index, item in enumerate(menu):
        print(f"{index} {item['name']} ${item['price']}")


def calc_total(orders):
    """ caculate the sum of the orders"""
    total = 0
    for order in orders:
        # print(f"the customer ordered: {menu[order]}")
        item = menu[order]
        # print(f"price: {item['price']}")
        total = total + item['price']
    print(total)

def show_orders(orders):
    """ show what you ordered"""
    print("orders:")
    for order in orders:
        item = menu[order]
        print(item['name'])



show_menu(menu)

print('welcome to daisys')

while True:
    ip = input('please enter item number \npress q to quit')
    if str(ip) == 'q':
        print('goodbye')
        sys.exit()
    print(ip)
    # adds orders to my list
    customer_orders.append(int(ip))
    print(f'customer_orders: {customer_orders}')

    show_orders(customer_orders)
    calc_total(customer_orders)







    # if str(ip) == '0'
    #     print('you have added ice cream')
    #     print ('the cost so far is'*total_cost)
    # if str(ip) == '1'
    #     print('you have added brownie')
    #     print('the cost so far is'*total_cost)
