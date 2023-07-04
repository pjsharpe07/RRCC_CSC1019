#############################
# initial function examples #
#############################

def add_two_number(number_one, number_two):
    sum = number_one + number_two
    return sum

values_added = add_two_number(5, 7)
print(values_added)
print(f'12 + 7 = {values_added}')



#############################
# void and return statements #
#############################

# def print_add_two_number(number_one, number_two):
#     sum = number_one + number_two
#     print(f'The sum of {number_one} and {number_two} is {sum}')

# print_add_two_number(14, 7)


#################################################
# removing the 'return' from non-void functions #
#################################################

# def add_two_number(number_one, number_two):
#     sum = number_one + number_two
    

# values_added = add_two_number(5, 7)
# print(values_added)
# print(f'12 + 7 = {values_added}')


#################################################
# create a print function but don't call it #
#################################################

# def print_and_say_hello(name):
#     print(f'Hi {name}! How are you today?')



# # invoke function here
# print_and_say_hello('Grace')


############################
# examples involving scope #
############################


# first_one = 'testing'

# def this_is_a_test():
#     second_one = 'testing again!'
#     return second_one

# print(first_one) # this is in the 'global' scope -- so it is good to print
# print(second_one) # this one won't print! Only lives in 'local' scope


####### and another one #############

# first_one = 'testing'

# def this_is_a_test():
#     first_one = 'changed value?'
#     second_one = 'testing again!'
#     return first_one + ' ' + second_one

# testing = this_is_a_test()
# print(testing)
# print(first_one) # 'testing'


#######################################
# parameter default and good practice #
#######################################


# def hi_there(name='Preston'):
#     print(f'Hello {name}')


# hi_there() # 'Hello Preston'
# hi_there('Nic') # 'Hello Nic'



######### testing with defaults and ordinal position

# def two_values(value_one, value_two=7): 
#     print(f'The first value is {value_one}')
#     print(f'The second value is {value_two}')

# two_values(22, 23)
##### The first value is 22
##### The second value is 23
# two_values(50)
##### The first value is 50
##### The second value is 7

################################################
# calling the specific name when using default #
################################################

# rounded_num = round(10.315) # default ndigits = 0 used here
# print(rounded_num)

# rounded_num = round(10.315, ndigits=1)
# print(rounded_num)

# rounded_num = round(ndigits=1, number=10.315) # this is the same as above!
# print(rounded_num)
