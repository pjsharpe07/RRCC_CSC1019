###################
## list examples ##
###################

my_list = ['Preston', 14, 33.3]
print(my_list) # ['Preston', 14, 33.3]

my_second_list = [True, False, my_list]
print(my_second_list) # [True, False, ['Preston', 14, 33.3]]

# ### accessing list value ###
# my_list = ['Preston', 14, 33.3]

# first_value = my_list[0] 
# print(first_value) # 'Preston'

# second_value = my_list[1]
# print(second_value) # 14

# last_value = my_list[-1]
# print(last_value) # 33.3


##### accessing more than one list value #####

# my_list = ['Preston',
#            14,
#            33.3,
#            True
#            ]

# new_list = my_list[1:3]
# print(new_list) # [14, 33.3]


########### list does not exist ######

# my_list = ['Preston', # 0
#            14, # 1
#            33.3, # 2
#            True # 3
#            ]

# my_value = my_list[4]
# print(my_value)
# # IndexError: list index out of range

##### updating list values #####

### strings cannot be updated in place

# my_name = 'preston'
# my_name[0] = 's'
# TypeError: 'str' object does not support item assignment

# my_list = ['Preston',
#            14,
#            33.3,
#            True
#            ]
# print(my_list) # ['Preston', 14, 33.3, True]

# my_list[0] = 'John'
# print(my_list) # ['Preston', 14, 33.3, True]