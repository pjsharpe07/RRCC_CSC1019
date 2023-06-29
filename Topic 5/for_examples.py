#########################################################
#### initial while loop example ####
#########################################################

# distance in cm
# nail_length = 5

# # each 'strike' brings you 1 cm closer
# # continue unitl NO cm left

# while nail_length > 0:
#     print(f'Hammering Nail...')
#     nail_length = nail_length - 1
#     # you can also do it this way!
#     # nail_length -= 1
#     print(f'Finished hammering. Nail length is now {nail_length}cm\n')
# else:
#     print('Done!')

#########################################################
#### while and user feedback ####
#########################################################


# user_response = input('Hi there. What is your name? You can exit this program by writing "Done". ')

# while user_response.lower() != "done":
#     print(f'Hi {user_response}! It is really nice to meet you.')
#     user_response = input('Tell me another name? ')
# else:
#     print('Goodbye! It was nice chatting with you.')


#########################################################
### infinite loop example ####
#########################################################

# number_of_tacos = 10

# while number_of_tacos != 5:
#     print('Time to eat some tacos! I have', number_of_tacos)
#     input("Tell me when you're ready to eat again!")
#     number_of_tacos += 1


#########################################################
### for loops and ranges! ####
#########################################################

# example 1:

# for i in range(10):
#     print(f'{i}. Hello')
# else:
#     print('Goodbye\n')

# # # example 2:

# for i in range(5, 10):
#     print(f'{i}. Hello')
# else:
#     print('Goodbye')


#########################################################
### for loops and lists! ####
#########################################################

# sith lords according to IGN https://www.ign.com/wikis/star-wars/Sith_Lords
# sith_lords = ['Darth Bane', 'Darth Tyranus', 'Darth Pagueis', 'Darh Sidious', 'Darth Maul', 'Darth Vader']

# for lord in sith_lords:
#     print(f'{lord} was a sith_lord')

#########################################################
### nested loops! ####
#########################################################

# Example One:

# number_of_rows = int(input('Enter row number: '))
# number_of_columns = int(input('Enter column number: '))

# for row in range(number_of_rows):
#     for column in range(number_of_columns):
#         print('*', end=' ') # the number of * to print is in the inner body
    
#     # start a new line here -- this is in the 'OUTER' body
#     print('#\n')


# Example Two:

# number_of_rows = int(input('Enter row number: '))
# number_of_columns = int(input('Enter column number: '))

# for r in range(number_of_rows):
#     for c in range(number_of_columns):
#         print(f'Row: {r} - Column: {c}', end=' *** ') # the number of * to print is in the inner body
    
#     # new line - in outer body!
#     print('')


#########################################################
### loops with appended lists ####
#########################################################


# finding the smallest number -- with if statements 

# input_number = int(input('Enter a number here: '))
# min_number = input_number

# # wait to input received is > 

# if input_number < 0:
#     print('No positive number provided')
# else:
#     while input_number > 0:
#         input_number =  int(input('Enter a number here: '))

#         # check for smaller value
#         if input_number < min_number and input_number >= 0:
#             min_number = input_number
#     # once loop break -- exit and output
#     else:
#         print('Smallest number is ', min_number)


## easier?


# input_number = int(input('Enter a number here: '))

# final_list = []

# if input_number < 0:
#     print('No positive number provided')
# else:
#     while input_number > 0:
#         final_list.append(input_number)
#         input_number = int(input('Enter a number here: '))
#     else: # once loop is broken -- output smallest
#         print(f'Smallest number is {min(final_list)}')