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


rain = input('Is it raining? ')
gas = input('Do you have gas? ')

is_raining = rain.lower() == 'yes'
has_gas = gas.lower() == 'yes'

if is_raining and has_gas:
    print(f"It's raining so I should drive")
elif is_raining and not has_gas:
    print(f"It's raining but I do not have gas! I should go get some.")
else:
    print('Clear day. I should ride my bike')