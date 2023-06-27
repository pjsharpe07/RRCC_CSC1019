### this is the example of an if statement ###

### convert to binary if input is > 0

user_num = int(input('Enter your number here:'))

if user_num < 0:
    print('Negative number passed. No binary provided.')
else:
    binary_number = bin(user_num)
    split_bin = binary_number.split('b')[1]
    
    print(f'{user_num} in binary is {split_bin}')
