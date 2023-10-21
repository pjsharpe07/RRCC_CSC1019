# reformatting time

input_time = input('What time is it? ')
hour = input_time[:2]
minute = input_time[3:]

print(f'The hour is {hour} and the minute is {minute}')

# reformatting phone number

phone_number = input('What number? ')

first_three = phone_number[:3]
middle_three = phone_number[3:6]
last_three = phone_number[6:]

phone_number = f'{first_three}-{middle_three}-{last_three}'
print(phone_number)