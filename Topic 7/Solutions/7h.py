# sample input 1: Robert000Smith000123
# sample input 2: 00000Steve00000Buscemi000007891


# get the encoded string as input
encoded_string = input('Encoded String: ')


### first find the index of the first zero

# this will be the sep of our split later
zero_string = ''

current_idx = encoded_string.index('0')

# find the length of the sting
while encoded_string[current_idx] == '0':
    zero_string = zero_string + '0'
    current_idx += 1

all_values = encoded_string.split(zero_string)
print(all_values) # ['Robert', 'Smith', '123']

# in case we start with the 0 string - remove the first '' element in list
if not all_values[0]:
    all_values.pop(0)

final_dict = {
    "first_name" : all_values[0],
    "last_name" : all_values[1],
    "id" : int(all_values[2])
}
print(final_dict)