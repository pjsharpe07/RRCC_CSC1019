input_numbers = input('What numbers are you checking? ').split()
# for example: 4, 7, 13, 5, 7

input_index = int(input('What index do you want removed? '))

input_numbers.pop(input_index)
print(input_numbers)