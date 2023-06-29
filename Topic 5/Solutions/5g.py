### generate the fibonacci sequence up to a point


sequence_number = int(input('How many fib numbers do you want? '))

# the first two should be hard coded
fibonacci_numbers = [0, 1]

# don't allow negative number inputs
if sequence_number == 0: # logic for the first two
    fibonacci_numbers = [0]
else:
    while len(fibonacci_numbers) != sequence_number:
        if sequence_number < 0:
            sequence_number = int(input('You must enter a number greater than zero. Try again? '))
        else:
            last_number = fibonacci_numbers[-1]
            second_to_last = fibonacci_numbers[-2]
            fibonacci_numbers.append(last_number + second_to_last)


for number in fibonacci_numbers:
    print(f'{number}', end=', ')

# need to convert these to string to use the join method -- this works!
# final_numbers = [str(x) for x in fibonacci_numbers]

# print(', '.join(final_numbers))