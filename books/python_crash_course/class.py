#Creating and using a Class
class Dog:
    """A simple attempt to mode a dog"""

    def __init__(self, name, age):
        """Initialize name and attributes"""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is sitting")

    def roll_over(self):
        """Simulate dog rolling over"""
        print(f" {self.name} roll over! ")


my_dog = Dog('karma', 16)
your_dog = Dog('spirit', 10)

print(f"\nMy dog's name is {my_dog.name}")
my_dog.sit()
print(f"\nMy dog's age is {my_dog.age}")
my_dog.roll_over()
print(f"\nYour dog's name is {your_dog.name}")
your_dog.sit()


#Restaurant Class Example #9-1 & 9-4
class Restaurant:
    """ Define a Restaurant using a class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and Attributes"""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """Describe the Restaurant in a function"""
        print(f"\nThe resteraunt {self.name} is serving {self.cuisine_type}. ")
        print(f"\n{self.name} is also not very expensive")

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        msg = f"{self.name} is open, come on in!"
        print(msg)

    def set_numbers_served(self, numbers_served):
        """Allow the user to set number of customers served"""
        self.numbers_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.numbers_served += additional_served


restaurant = Restaurant('Karmines', 'Steak')
print(restaurant.name)
print(restaurant.cuisine_type)
print(f"\nNumber served: {restaurant.numbers_served}")
restaurant.numbers_served = 430
print(f"Number served: {restaurant.numbers_served}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

draught_house = Restaurant('Draught House', 'Burgers')
draught_house.describe_restaurant()

chinese_buffet = Restaurant('Chinese Buffet', 'Orange Chicken')
chinese_buffet.describe_restaurant()

namys = Restaurant('Namys', 'Sushi')
namys.describe_restaurant()


#User class example
class User():
    """Represents a simple User Profile"""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.email = email.title()
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of a user"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """ Display a peronalized Greeting to the User"""
        print(f"\n Welcome Back {self.username}! ")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0

blake = User('blake', 'reidinger', 'aresbr117', 'Breidinger98@hotmail.com',
                'New Jersey')
blake.describe_user()
blake.greet_user()

print('\nMaking 3 login attempts...')
blake.increment_login_attempts()
blake.increment_login_attempts()
blake.increment_login_attempts()
print(f"  Login attempts: {blake.login_attempts}")

print("\nResetting login attempts...")
blake.reset_login_attempts()
print(f"  Login attempts: {blake.login_attempts}")





#Working with classes and instances.  The Car class

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """Print a statement showing the cars milage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def get_descriptive_name(self):
        """Return a neatly formmated descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back the odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    #The __init__()Method for a Child class
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self,make,model,year):
        """initialize attributes of the parent class."""
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())




my_new_car = Car('dodge', 'charger', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
