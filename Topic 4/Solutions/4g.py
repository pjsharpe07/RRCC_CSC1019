total_minutes = int(input('How many minutes are we calculating? '))

num_hours = total_minutes // 60
num_minutes = total_minutes % 60

print(f'{total_minutes} minutes is the same as {num_hours} hours and {num_minutes} minutes')