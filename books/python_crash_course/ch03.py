a_boolean = True
the_other_boolean = False
print(f'is boolean {a_boolean}')
print(the_other_boolean)
is_one_equal_to_two = 1 == 2
print(is_one_equal_to_two)
is_one_greater_than_two = 1 > 2
print(is_one_greater_than_two)
is_one_greater_than_or_equal_to_two = 1 >= 2
print(is_one_greater_than_or_equal_to_two)
is_one_less_than_two = 1 < 2
print(is_one_less_than_two)
is_one_less_than_or_equal_to_two = 1 <= 2
print(is_one_less_than_two)
is_one_not_equal_to_two = 1 != 2
print(is_one_not_equal_to_two)
print(True is False)
is_thirty_seven_greater_than_twenty_nine = 37 > 29
print(is_thirty_seven_greater_than_twenty_nine)
if 37 < 40:print('Thirty seven is less than 40')
age = 31
if age >= 35:print('You are old enough to be the president.')
else:print('You are not old enough to be the President')
print('Have a nice day')
age = 29
if age >= 35:print('You are old enough to be a Senator or the President')
elif age >= 30:print('You are old enough to be a Senator')
else:print('You are not old enough to be a Senator or the President')
print('Have a nice day!')
age = 99
if age >= 35:print('You are old enough to be a Representative,Senator, or the President.')
elif age >= 30:print('You are old enough to be a Senator.')
elif age >= 25:print('You are old eough to be a Representative.')
else:print('You are not old enough to be a Representative,Senator, or the President.')
print('Have a nice day')
distance = input('How far would you like to travel in miles')
distance = int(distance)
if distance < 3:mode_of_transport = 'walking'
elif distance < 300:mode_of_transport = 'driving'
else:mode_of_transport = 'flying'
print('I suggest {} to your destination.'.format(mode_of_transport))
