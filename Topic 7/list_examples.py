##############################
### access single element ####
##############################


# my_fake_list = [
#     'Preston',
#     22,
#     'Hello!',
#     'Good Morning!'
# ]

# # print(my_fake_list)
# # # ['Preston', 22, 'Hello!', 'Good Morning!']

# # # printing values of list
# # print(my_fake_list[0]) # first one  - 'Preston'
# # print(my_fake_list[1]) # second one - 22

# my_fake_list = [
#     'Preston',
#     22,
#     'Hello!',
#     'Good Morning!'
# ]

# first_two_of_list = my_fake_list[0:2]
# print(first_two_of_list)
# #  ['Preston', 22]

# first_two_of_list = my_fake_list[:2]
# print(first_two_of_list)
# #  ['Preston', 22]


# my_fake_list = [
#     'Preston',
#     22,
#     'Hello!',
#     'Good Morning!'
# ]


# third_to_end = my_fake_list[2:]


###############################
### last element of a list ####
###############################


# my_fake_list = [
#     'Preston',
#     22,
#     'Hello!',
#     'Good Morning!'
# ]

# print(my_fake_list[-1])
# print(my_fake_list[len(my_fake_list)]) # this fails, why?



########################
### updating a list ####
########################

# my_fake_list = [
#     'Preston',
#     22,
#     'Hello!',
#     'Good Morning!'
# ]

# my_fake_list[0] = 'Victor'
# print(my_fake_list)
# # ['Victor', 22, 'Hello!', 'Good Morning!']


########################
### knowledge check ####
########################

my_favorite_things = [
    'Rapids',
    'burritos',
    'DND',
    'piano',
    'video games',
    'hiking'
]


############# KC 1 ##################

# print(my_favorite_things[2])

############# KC 2 ##################

# print(my_favorite_things[:3])

############# KC 3 ##################

# my_favorite_things[-1] = my_favorite_things[-1] + ' and camping'
# print(my_favorite_things)


#########################################
############## list split ###############
#########################################

# string_of_names = 'Victor, Tim, Robert, Eliah'

# names_list = string_of_names.split(', ')
# print(names_list)
# ['Victor', 'Tim', 'Robert', 'Eliah']

############# using the default ###############

# string_of_names = 'Victor Tim Robert Eliah'

# names_list = string_of_names.split()
# print(names_list)
# # ['Victor', 'Tim', 'Robert', 'Eliah']
# print(len(names_list)) # 4


############# Different Character ###############

# string_of_names = 'Victor-Tim-Robert-Eliah'

# names_list = string_of_names.split('-')
# print(names_list)
# # ['Victor', 'Tim', 'Robert', 'Eliah']
# print(len(names_list)) # 4



############### potential gotcha #############

# string_of_names = 'Victor Tim Robert Eliah'

# names_list = string_of_names.split(', ')
# print(names_list)
# # ['Victor Tim Robert Eliah']
# print(len(names_list)) # 1

############ Using split ####################

### the 'old' method - constantly getting input
### determine if a positive number is even or odd

# user_number = int(input('Enter a number here. Enter a negative number to exit: '))

# while user_number > 0:
#     if user_number % 2 == 0:
#         print(f'{user_number} is even')
#     else:
#         print(f'{user_number} is odd')
    
#     user_number = int(input('Enter a number here. Enter a negative number to exit: '))
    
### only one input and using list?
### determine if each number is positive or negative

# user_input = input('What numbers do you want to check?').split()
# # print(user_input)

# for number in user_input:
#     try:
#         checking_number = int(number)
#         if checking_number % 2 == 0:
#             print(f'{checking_number} is even!')
#         else:
#             print(f'{checking_number} is odd')
#     except:
#         print(f'{number} cannot be converted to an integer')

##############################################
############ joining with a list #############
##############################################

# my_fake_list = ['hello', 'goodbye', 'final thing']

# new_value = ', '.join(my_fake_list)
# print(new_value)
# hello, goodbye, final thing


#############################################
############ using append and join ##########
#############################################

# name_list = input('What names do you want checked? ').split()
# input_letter = input('What letter do you want checked? ')
# # this is the final list we'll append to if the criteria is correct
# final_list = []

# for name in name_list:
#     if name[0].lower() == input_letter.lower():
#         final_list.append(name)

# final_value = ', '.join(final_list)
# print(f'The names that start with {input_letter} are {final_value}')

# for input: Sam Rebecca Margot Sebastian Chris Nic Sally
## ouput: The names that start with S are Sam, Sebastian, Sally

#############################################
############ list comprehension #############
#############################################

##### adding 5 to each value in list

# my_list = [14, 7, -10, 100]
# my_new_list = [x + 5 for x in my_list]
# print(my_new_list)
# [19, 12, -5, 105]

#### how to quickly convert all strings to integers?

# my_numbers = ['7', '44', '100', '-1000']
# # print(sum(my_numbers)) # this one fails
# my_integers = [int(x) for x in my_numbers]
# print(my_integers)
# # [7, 44, 100, -1000]
# print(sum(my_integers)) # -849


#### filtering all negative numbers in a list

### you can use an if statement

my_integers = [55, 14, 33, 18, -100]

even_numbers = [x for x in my_integers if x % 2 == 0]
print(even_numbers)
# [14, 18, -100]

### adding 5 to all odd numbers
odd_plus_five = [x + 5 for x in my_integers if x % 2 != 0]
print(odd_plus_five)
# [60, 38]
