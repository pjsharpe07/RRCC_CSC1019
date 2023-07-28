################################
###### make change example #####
################################

change_needed = int(input('How much change do you need? '))

num_twenty = change_needed // 20
num_ones = change_needed % 20

print(f'You will need {num_twenty} $20(s) and {num_ones} $1(s)')