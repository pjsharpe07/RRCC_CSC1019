### output middle character of string

input_string = input('Enter an input string: ')

string_length = len(input_string)
middle_character = string_length // 2 # the first/only middle character

if string_length % 2 != 0:
    middle = input_string[middle_character]
else:
    middle = input_string[middle_character - 1: middle_character + 1]

print(f'The middle character(s) of {input_string} is {middle}')
