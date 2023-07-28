my_name = input('What name do you want to try? ')

first_letter = my_name[0]
last_letter = my_name[-1]
# OR 
last_letter = my_name[len(my_name) - 1]

print('First letter:', first_letter)
print('Last Letter:', last_letter)


# Challenge!!!!

name_length = len(my_name)
middle_value = name_length // 2

if name_length % 2 == 0:
    middle_letter = my_name[middle_value - 1: middle_value + 1]
else:
    middle_letter = my_name[middle_value]

print('Middle Letter(s):', middle_letter)