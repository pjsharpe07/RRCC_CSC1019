### boolean example

# print(2 + 2 == 4) # True
# print(2 + 2 == 5) # False


##### if - else example

# test_string = 'testing'

# if test_string == 'testing':
#     print('They match!')
# else:
#     print('They do not match')


##### input example ####

# first_number = int(input('First number:'))
# second_number = int(input('Second number:'))

# if first_number > second_number:
#     print(f'{first_number} is larger than {second_number}')
# else:
#     print(f'{second_number} is larger than {first_number}')


#### elif examples #### 

# first_number = int(input('First number:'))
# second_number = int(input('Second number:'))

# if first_number > second_number:
#     print(f'{first_number} is larger than {second_number}')
# elif first_number == second_number:
#     print(f'{first_number} is the same as {second_number}')
# else:
#     print(f'{second_number} is larger than {first_number}')


########## and/or/not example ################


day_of_week = 'Friday'
money_in_account = 30

if day_of_week == 'Friday' and money_in_account >= 20:
    print('You can get delivery')
else:
    print('Sorry, no delivery today')



# rain = input('Is it raining? ')
# gas = input('Do you have gas? ')

# is_raining = rain.lower() == 'yes'
# has_gas = gas.lower() == 'yes'

# if is_raining and has_gas:
#     print(f"It's raining so I should drive")
# elif is_raining and not has_gas:
#     print(f"It's raining but I do not have gas! I should go get some.")
# else:
#     print('Clear day. I should ride my bike')


########## 'in' example ################


# create a list of plants in your garden
# note the CASING here -- all lower
garden_plants = [
    'tomatoes',
    'cucumbers',
    'mint',
    'squash',
    'basil',
]

plant_to_check = input('What plant would you like to check? ')

# must lower case to find in the list
plant_lower = plant_to_check.lower()

if plant_lower in garden_plants:
    print('We have', plant_to_check)
else:
    print(f'Sorry, {plant_to_check} do(es) not exist in the garden.')
