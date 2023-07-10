from datetime import datetime, timedelta


# fetching all of the user inputs
add_or_sub = input('Are you adding or subtracting minutes? ')

while add_or_sub.lower() not in ('add', 'subtract'):
    print(f'You entered {add_or_sub} - valid options are "add" or "subtract"')
    add_or_sub = input('Try again? ')

# determine minutes as pos/negative
if add_or_sub.lower() == 'subtract':
        minutes = - int(input('How many minutes do you want to subtract? ')) # need to make this negative
else:
    minutes = int(input('How many minutes do you want to subtract? '))


# Using current time
right_now = datetime.now()

final_time = right_now = right_now + timedelta(minutes = minutes)
print(f'Changing current time by {minutes} minutes yields {final_time}')