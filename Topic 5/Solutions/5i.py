from statistics import mean

# average calculation #


input_number = int(input('What is the next number. Enter a negative to exit: '))

# average this set at the end
all_numbers = []

if input_number < 0:
    print('No positive numbers provided. No average calcuation completed')
else:
    while input_number > 0:
        all_numbers.append(input_number)
        input_number = int(input('What is the next number. Enter a negative to exit: '))

string_numbers = [str(x) for x in all_numbers]

print(f'The average of the numbers {", ".join(string_numbers)} is: {mean(all_numbers)}')