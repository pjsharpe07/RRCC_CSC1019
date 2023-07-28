########### first print/variable statements ######

wage = 20
hours = 40
weeks = 52
salary = wage * hours * weeks

print('Salary is', salary)

# now change hours to 25
hours = 35
salary = wage * hours * weeks

print('New salary is', salary)


###############################################
####### multiple ways to print statements #####
###############################################

# # these all work the same
# favorite_country = 'Spain'

# # the '+' method
# print('My favorite country to visit is ' + favorite_country + ' while on vacation')

# # the ',' method
# print('My favorite country to visit is',  favorite_country, 'while on vacation')

# # the formatted string method
# print(f'My favorite country to visit is {favorite_country} while on vacation')


# # the '+' method - the gotcha
# wage = 20
# hours = 40
# weekly_salary = wage * hours

# ###### these fail! ###########
# print('Working ' + hours + 'hours per week with a wage of ' + wage + '...')
# print('Will get you $' + str(weekly_salary))


# ###### these work! ###########
# print('Working ' + str(hours) + 'hours per week with a wage of ' + str(wage) + '...')
# print('Will get you $' + str(weekly_salary))

#############################################
############# 4.8 from book #################
#############################################

# hourly_wage = 20

# print('Annual salary is: ')
# print(hourly_wage * 40 * 50)
# print()

# print('Monthly salary is: ')
# print(((hourly_wage * 40 * 50) / 1))
# print()

# FIXME: The above is wrong. Change 
#        the 1 so that the statement
#        outputs monthly salary.


######################################
######## using 'end' with print ######
######################################

# print('Hello World!')
# print('This is on a new line')
# print('First sentence.', end=' ')
# print('Second sentence.')
# Hello World!
# This is on a new line
# First sentence. Second sentence.

######################################
######## getting user input ##########
######################################

# # just straight up input
# favorite_food = input()
# print('My favorite food is', favorite_food)

# # with a prompt
# favorite_food = input('What is your favorite food? ')
# print('My favorite food is', favorite_food)

######################################
#### getting more than one input #####
######################################

# first_name = input()
# last_name = input()

# using prompts
# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')

# print('First input is', first_name)
# print('Second input is', last_name)

# print(f'Hello {first_name} {last_name}.', end=' ')
# print('How are you?')

#####################################
####### overwriting variables #######
#####################################

# x = 4
# y = 7
# z = x + y

# z = 5

# print(z)

#####################################
####### getting data types ##########
#####################################

# my_age = input()

# in_five_years = my_age + 5
# print(f'In five years, I will be {in_five_years} years old')

#### understanding data types
# print(type('my string')) # <class 'str'>
# print(type(44)) # <class 'int'>
# print(type(33.3)) # <class 'float'>
# print(type([4, 33, 'hello', 22.2222])) # <class 'list'>

##### convert a data type
# my_value = '44'
# print(type(my_value)) # <class 'str'>
# my_value = int(my_value)
# print(type(my_value)) # <class 'int'>

##### what is wrong here? 
# my_value = 'Hello there!'
# my_value = int(my_value)
# print(type(my_value))



### input and data types ####
# my_age = input()
# print(type(my_age)) 