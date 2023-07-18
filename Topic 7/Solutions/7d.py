input_numbers = input('What numbers do you want to find? ').split(';')
# input for example: 13;77;-100;55

input_numbers = [int(x) for x in input_numbers]
min_number = min(input_numbers)
max_number = max(input_numbers)

print(f'Min is: {min_number}. Max is: {max_number}')