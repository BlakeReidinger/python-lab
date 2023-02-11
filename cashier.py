import sys 

menu = [
    { 'name': 'Big Mac', 'price': 6.50},
    { 'name': 'Fries', 'price': 4.00},
    { 'name': 'Chicken Nuggets', 'price': 5.00},
    { 'name': 'Bacon Mcdouble', 'price': 6.00},
    { 'name': 'Milkshake', 'price': 3.00},   
]

customer_orders = []


def show_menu(menu):
    """Display Menu on Screen"""
    #Display the name value and the Price value
    for key,value in enumerate(menu):
        print(f" {key} {value['name']} ${value['price']}")

print("Welcome to Mcdonalds.")
show_menu(menu)

def calc_totals(orders):
    """Calculate the total for all orders"""
    total = 0
    for order in orders:
        value = menu[order]
        total = total + value['price']
    print(total)

def display_orders(orders):
    """Display what the customer has ordered"""
    for order in orders:
        value = menu[order]
        print(value['name'])
        
while True:
    prompt = str(input("Welcome to Mcdonalds how can I help you today?\nPress 'Q' at any time to exit: "))
    if str(prompt) == 'Q':
        print("Have a nice day!")
        sys.exit()
    print(prompt)
    #Adding orders
    customer_orders.append(int(prompt))
    print(f"Here is your order summary: {customer_orders}")
    
    display_orders(customer_orders)
    calc_totals(customer_orders)
 
        
        
    