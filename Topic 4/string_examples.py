############################
## using the len function ##
############################

# my_name = 'Preston'
# print(len(my_name)) # 7


# string indexing

# my_name = 'Preston'
# first_letter = my_name[0]
# second_letter = my_name[1]

# print(first_letter) # 'P'
# print(second_letter) # 'r'


######### getting multiple 'slices' ####

# my_name = input('What name do you want to try? ') # assume Preston is input

# # first method
# first_three_letters = my_name[0:3]
# print(first_three_letters) # Pre

# # second method
# first_three_letters = my_name[:3]
# print(first_three_letters) # Pre


#### another example ####

my_name = input('What name do you want to try? ') # assume Preston is input

third_and_fourth = my_name[2:4]
print(third_and_fourth) # es

fifth_to_end = my_name[4:]
print(fifth_to_end) # ton